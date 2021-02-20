from django import forms
from .models import *


def number_school(school_id):
    return school_id


class StudentsForm(forms.Form):
    keySchool = forms.CharField(max_length=300, label='Фамилия', initial=number_school(school_id=1))
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


class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField(widget=forms.PasswordInput())