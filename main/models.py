from django.db import models
from django.urls import reverse


class Period(models.Model):
    title = models.CharField(max_length=300, verbose_name='Период')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def get_absolute_url(self):
        return reverse('period_detail', args=[str(self.id)])


class Students(models.Model):
    keyPeriod = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='period',
                                    verbose_name='Период')
    surname = models.CharField(max_length=300, verbose_name='Фамилия')
    name = models.CharField(max_length=300, verbose_name='Имя')
    patronymic = models.CharField(max_length=300, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'
