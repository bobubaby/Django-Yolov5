# Generated by Django 4.1 on 2023-08-01 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classbehavior', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
