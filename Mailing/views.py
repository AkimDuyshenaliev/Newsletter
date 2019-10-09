import os

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail, send_mail
from django.conf import settings
from django.core import mail
from django.urls import reverse_lazy

from rest_framework import viewsets

from .forms import *
from .models import *
from .serializers import *

# Create your views here.


class HomeView(TemplateView):
    name = 'Mailing/index.html'

    def get(self, request):
        form = IndexForm()
        return render(request, self.name, {'form': form})

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():  
            form.save()

            connection = mail.get_connection()
            connection.open()

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_from = settings.EMAIL_HOST_USER

            get_department = form.cleaned_data['department'] # Recive the department name
            print(get_department)

            department = DepartmentModel.objects.filter(name__icontains=get_department).values('id')  # Search for department in field and get 'id' of the field
            print(department)

            raw_emails = list(UserModel.objects.filter(department__in=department).values_list('email')) #get filtered by id list of emails
            print(raw_emails)

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

            print(to_list)


            ##### Read emails from char field ######
            # to_list = form.cleaned_data['email']
            # to_list = to_list.split(', ')
            
            ###### Read emails from file ######
            # file = SaveTextFileModel.objects.all().get(id=0).fileTXT
            # file.open(mode='rb')
            # content = file.read()
            # to_list = content
            # print(to_list)
            # file_with_emails = open(os.path.join(settings.BASE_DIR, 'filename'))

            recipient_list = to_list

            send_mail(subject, message, email_from, recipient_list,
                      connection=connection, fail_silently=False)

            connection.close()
        
        return render(request, self.name, {'form': form})


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
