import os

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail, send_mail
from django.conf import settings
from django.core import mail

from .forms import *
from .models import *

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


            to_list = form.cleaned_data['email']
            to_list = to_list.split(', ')
            
            file = SaveTextFileModel.objects.all().get(id=0).fileTXT
            file.open(mode='rb')
            content = file.read()
            to_list = content
            print(to_list)
            # file_with_emails = open(os.path.join(settings.BASE_DIR, 'filename'))

            recipient_list = to_list

            send_mail(subject, message, email_from, recipient_list,
                      connection=connection, fail_silently=False)

            connection.close()
        
        return render(request, self.name, {'form': form})
