# Generated by Django 3.0.9 on 2021-02-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_students_snils'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата обучения'),
        ),
    ]
