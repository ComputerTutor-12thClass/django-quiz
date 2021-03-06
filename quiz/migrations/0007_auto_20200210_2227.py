# Generated by Django 2.2.10 on 2020-02-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200210_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='has_image',
            field=models.BooleanField(default=False, help_text='Does question have image?', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='question',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
