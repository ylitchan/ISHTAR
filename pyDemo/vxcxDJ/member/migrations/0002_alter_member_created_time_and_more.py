# Generated by Django 4.1.7 on 2023-03-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='oauthmemberbind',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
