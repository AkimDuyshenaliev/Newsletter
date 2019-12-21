import datetime
from celery import shared_task
from time import sleep

import os

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail, send_mail
from django.conf import settings
from django.core import mail
from django.urls import reverse_lazy
from datetime import date

from .forms import *
from .models import *
from .serializers import *


form = IndexForm()


@shared_task
def send_email():
    if form.is_valid():
        connection = mail.get_connection()
        connection.open()


        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_from = settings.EMAIL_HOST_USER

        # Recive the department name
        get_department = form.cleaned_data['department']

        department = DepartmentModel.objects.filter(name__icontains=get_department).values('id')  # Search for department in field and get 'id' of the field

        raw_emails = list(UserModel.objects.filter(department__in=department).values_list('email'))  # get filtered by id list of emails

        #Prepare the list of emails
        to_list = []
        temp = [None] * len(raw_emails)
        last_iteration = len(raw_emails) - 1

        if len(raw_emails) == 1:
            to_list = list(raw_emails[0])
        else:
            for _ in range(len(raw_emails)):
                temp[_] = list(raw_emails[_])
                if last_iteration:
                # At the last iteration merge all elements into one list
                    to_list += temp[_]

        recipient_list = to_list

        send_mail(subject, message, email_from, recipient_list,connection=connection, fail_silently=False)

        connection.close()

        print("Email (celery task) successfully sent!")




# here we assume we want it to be run every 5 mins
# @celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
# def myTask():
#     # Do something here
#     # like accessing remote apis,
#     # calculating resource intensive computational data
#     # and store in cache
#     # or anything you please
#     print 'This wasn\'t so difficult'
