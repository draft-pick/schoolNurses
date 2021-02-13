from django.db import models
from django.urls import reverse


class Period(models.Model):
    title = models.CharField(max_length=300, verbose_name='Период')
    date = models.DateField(null=True, verbose_name='Дата обучения')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def get_absolute_url(self):
        return reverse('view_period', kwargs={"period_id": self.pk})


class Students(models.Model):
    keyPeriod = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='period',
                                    verbose_name='Период')
    surname = models.CharField(max_length=300, verbose_name='Фамилия')
    name = models.CharField(max_length=300, verbose_name='Имя')
    patronymic = models.CharField(max_length=300, verbose_name='Отчество')
    snils = models.CharField(max_length=100, verbose_name='СНИЛС')
    SEX = (
        ('m', 'Мужской'),
        ('w', 'Женский'),
    )
    birthday = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='Пол')

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'
