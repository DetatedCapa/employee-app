from django import forms
from .models import Employee



class SaveEmployee(forms.ModelForm):
     class Meta:
       model = Employee
       fields = ['name', 'identity_number', 'department', 'address', 'salary']


