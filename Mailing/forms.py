from django import forms
from .models import SaveTextFileModel, DepartmentModel

from datetime import date


class IndexForm(forms.Form):

    schedule = forms.DateField(label='Pick when to send the newsletter (leave as is to send immediately)',
                               widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 
                                                             'required': 'false', 'value': date.today()}))

    ### Find the department names and populate CharField choices widget with them
    departmentChoicesTemp = list(DepartmentModel.objects.filter().values_list('name'))
    departmentChoices = []
    temp = [None] * len(departmentChoicesTemp)
    last_iteration = len(departmentChoicesTemp) - 1

    if len(departmentChoicesTemp) == 1:
        departmentChoices = list(departmentChoicesTemp[0])
    else:
        for _ in range(len(departmentChoicesTemp)):
            temp[_] = list(departmentChoicesTemp[_])
            if last_iteration:
                departmentChoices += temp[_]

    departmentChoices2 = departmentChoices
    departmentChoices = list(zip(departmentChoices, departmentChoices2))

    department = forms.CharField(
        label='Choose department to send email to', widget=forms.Select(choices=departmentChoices, attrs={'class': 'form-control'}))

    subject = forms.CharField(
        max_length=100, required=True, label='Subject field', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 70, 'class': 'form-control'}), required=True, label='Message field')
