# Generated by Django 4.2.11 on 2024-03-27 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
