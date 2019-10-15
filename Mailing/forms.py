from django import forms
from .models import SaveTextFileModel, DepartmentModel


class IndexForm(forms.Form, forms.ModelForm):

    # department = DepartmentModel.objects.all().values('name')

    departmentChoices = [
        ('python backend', 'python backend'),
        ('js', 'JS'),
        ('iOS', 'iOS')
    ]

    # email = forms.CharField(widget=forms.Textarea(
    #     attrs={'rows':1, 'cols':100}), required = False, label = 'Email field') #Email area

    department = forms.CharField(
        label='Choose department to send email to', widget=forms.Select(choices=departmentChoices))

    subject = forms.CharField(
        max_length=100, required=True, label='Subject field')
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 70}), required=True, label='Message field')

    # class Meta:
    #     model = SaveTextFileModel
    #     fields = ['fileTXT', ]
