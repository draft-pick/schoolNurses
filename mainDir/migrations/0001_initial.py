# Generated by Django 3.0.9 on 2021-02-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Период')),
                ('start_date', models.DateField(null=True, verbose_name='Дата начала обучения')),
                ('end_date', models.DateField(null=True, verbose_name='Дата окончания обучения')),
                ('is_active', models.CharField(choices=[('1', 'Активный'), ('0', 'В архив')], max_length=1, verbose_name='Активный?')),
            ],
            options={
                'verbose_name': 'Период обучения',
                'verbose_name_plural': 'Периоды обучения',
            },
        ),
    ]