# Generated by Django 4.1.7 on 2023-03-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WxShareHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField()),
                ('share_url', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
