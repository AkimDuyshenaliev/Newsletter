import os

from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
# from django.urls import reverse_lazy
from datetime import date

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .forms import *
from .models import *
from .serializers import *
from .tasks import *


class HomeView(TemplateView):
    name = 'Mailing/index.html'

    def get(self, request):
        form = IndexForm()
        return render(request, self.name, {'form': form})

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():  
            # form.save()

            connection = mail.get_connection()
            connection.open()


            selected_date = form.cleaned_data['schedule']
            today = date.today()

            time_left = selected_date - today

            if selected_date != today:
                send_email.delay()
            else:
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                email_from = settings.EMAIL_HOST_USER

                get_department = form.cleaned_data['department'] # Recive the department name

                department = DepartmentModel.objects.filter(name__icontains=get_department).values('id')  # Search for department in field and get 'id' of the field

                raw_emails = list(UserModel.objects.filter(department__in=department).values_list('email')) #get filtered by id list of emails

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
                            to_list += temp[_] #At the last iteration merge all elements into one list


                recipient_list = to_list

                send_mail(subject, message, email_from, recipient_list,
                        connection=connection, fail_silently=False)

                print("Email (now) successfully sent!")

            connection.close()
        
        context = {
            'form': form,
        }

        if Response(HomeView, status=status.HTTP_200_OK):
            context['success'] = "The message is sent!"
        else:
            context['error'] = "Error, something went wrong"

        return render(request, self.name, context)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
