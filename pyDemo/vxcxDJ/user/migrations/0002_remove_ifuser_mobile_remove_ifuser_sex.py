# Generated by Django 4.1.7 on 2023-02-27 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ifuser',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='ifuser',
            name='sex',
        ),
    ]
