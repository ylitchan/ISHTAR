# Generated by Django 3.2.5 on 2023-05-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alphaApp', '0003_auto_20230508_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallerInfo',
            fields=[
                ('tweet_id', models.TextField(primary_key=True, serialize=False)),
                ('tweet_user', models.TextField(blank=True, null=True)),
                ('tweet_alpha', models.TextField(blank=True, null=True)),
                ('tweet_text', models.TextField(blank=True, null=True)),
                ('tweet_media', models.TextField(blank=True, null=True)),
                ('tweet_gpt', models.TextField(blank=True, null=True)),
                ('alpha_time', models.TextField(blank=True, null=True)),
                ('alpha_datetime', models.DateTimeField(blank=True, null=True)),
                ('user_thumb', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='AlphaInfo',
            new_name='LaunchInfo',
        ),
    ]
