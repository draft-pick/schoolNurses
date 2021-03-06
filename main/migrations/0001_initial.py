# Generated by Django 3.0.9 on 2021-02-10 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Период')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=300, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=300, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('keyPeriod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period', to='main.Period', verbose_name='Период')),
            ],
            options={
                'verbose_name': 'Студенты',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
