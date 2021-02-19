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
        return reverse('view_period', kwargs={"period_id": self.pk})

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