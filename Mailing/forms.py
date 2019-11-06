from django import forms
from .models import SaveTextFileModel, DepartmentModel


class IndexForm(forms.Form):

    # departmentChoicesTemp = list(DepartmentModel.objects.filter().values('name'))
    # for _ in len(departmentChoicesTemp):
    #     for value in dict.departmentChoicesTemp(_):
    #         temp = [value]
    #         dictlist.append(temp)

    # departmentChoices = list(zip())

    departmentChoices = [
        ('python backend', 'python backend'),
        ('js', 'JS'),
        ('iOS', 'iOS')
    ]

    # email = forms.CharField(widget=forms.Textarea(
    #     attrs={'rows':1, 'cols':100}), required = False, label = 'Email field') #Email area

    department = forms.CharField(
        label='Choose department to send email to', widget=forms.Select(choices=departmentChoices, attrs={'class': 'form-control'}))

    subject = forms.CharField(
        max_length=100, required=True, label='Subject field', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 70, 'class': 'form-control'}), required=True, label='Message field')
