from django import forms
from .models import *


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['keySchool', 'surname', 'name', 'patronymic', 'birthday', 'sex', 'snils', 'contract_date', 'contract_number']


class StudentFormEdit(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
