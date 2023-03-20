# Generated by Django 4.1.7 on 2023-03-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_created=True)),
                ('nickname', models.TextField()),
                ('mobile', models.TextField()),
                ('sex', models.IntegerField()),
                ('avatar', models.TextField()),
                ('reg_ip', models.TextField()),
                ('status', models.IntegerField()),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OauthMemberBind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_created=True)),
                ('member_id', models.IntegerField()),
                ('client_type', models.TextField()),
                ('type', models.IntegerField()),
                ('openid', models.TextField()),
                ('unionid', models.TextField()),
                ('extra', models.TextField()),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
