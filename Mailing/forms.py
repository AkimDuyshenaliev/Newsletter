from django import forms
from .models import *


class IndexForm(forms.Form, forms.ModelForm):
    email = forms.CharField(widget=forms.Textarea(
        attrs={'rows':1, 'cols':100}), required = False, label = 'Email field')
    subject = forms.CharField(
        max_length=100, required=True, label='Subject field')
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 70}), required=True, label='Message field')

    class Meta:
        model = SaveTextFileModel
        fields = ['fileTXT', ]
