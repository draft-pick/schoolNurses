# Generated by Django 3.0.9 on 2021-02-16 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='is_active',
        ),
    ]
