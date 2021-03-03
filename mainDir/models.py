from django import forms
from django.db import models
from django.urls import reverse
from django.contrib.admin.widgets import AdminDateWidget


class Periods(models.Model):
    ACTIVE_CHOICES = (
        ('1', 'Активный'),
        ('0', 'В архив'),
    )
    title = models.CharField(max_length=300, verbose_name='Период наименование')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.CharField(max_length=1, choices=ACTIVE_CHOICES, verbose_name='Активный?')

    def get_absolute_url(self):
        return reverse('view_school', kwargs={"school_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Период обучения'
        verbose_name_plural = 'Периоды обучения'


class PeriodsForm(forms.ModelForm):
    start_date = forms.DateField(widget=AdminDateWidget, label="Дата начала обучения")
    end_date = forms.DateField(widget=AdminDateWidget, label="Дата окончания обучения")

    class Meta:
        model = Periods
        fields = ['title', 'is_active', 'start_date', 'end_date']


def number_school(school_id):
    return school_id


class Students(models.Model):
    keySchool = models.ForeignKey(Periods, on_delete=models.CASCADE, related_name='school',
                                  verbose_name='Школа')
    surname = models.CharField(max_length=300, verbose_name='Фамилия')
    name = models.CharField(max_length=300, verbose_name='Имя')
    patronymic = models.CharField(max_length=300, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    SEX = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='Пол')
    snils = models.CharField(max_length=100, verbose_name='СНИЛС')
    contract_date = models.DateField(verbose_name='Дата контракта')
    contract_number = models.CharField(max_length=300, verbose_name='Номер контракта')

    def __str__(self):
        return self.surname

    # def get_absolute_url(self):
    #     return reverse('open_student', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('view_student', kwargs={"student_id": self.pk})

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'



