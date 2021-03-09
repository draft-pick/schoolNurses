from django import forms
from .models import *


class StudentsForm(forms.Form):
    keySchool = forms.CharField(max_length=300, label='Фамилия')
    surname = forms.CharField(max_length=300, label='Фамилия')
    name = forms.CharField(max_length=300, label='Имя')
    patronymic = forms.CharField(max_length=300, label='Отчество')
    birthday = forms.DateField(widget=AdminDateWidget, label='Дата рождения')
    SEX = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    sex = forms.ChoiceField(choices=SEX, label='Пол')
    snils = forms.CharField(max_length=100, label='СНИЛС')
    contract_date = forms.DateField(widget=AdminDateWidget, label='Дата контракта')
    contract_number = forms.CharField(max_length=300, label='Номер контракта')

    class Meta:
        model = Students
        fields = ['keySchool', 'surname', 'name', 'patronymic', 'birthday', 'sex', 'snils', 'contract_date', 'contract_number']


class StudentFormEdit(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
