# Generated by Django 2.2.10 on 2020-02-08 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200208_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='name_1',
            field=models.CharField(max_length=100, verbose_name='Participant 1 Name'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='name_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Participant 2 Name'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number_1',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^\\+?1?\\d{9,15}$')], verbose_name='Participant 1 Phone Number'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^\\+?1?\\d{9,15}$')], verbose_name='Participant 2 Phone Number'),
        ),
    ]
