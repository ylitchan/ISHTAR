# Generated by Django 4.1.7 on 2023-04-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlphaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.TextField()),
                ('tweet_user', models.TextField()),
                ('tweet_text', models.TextField()),
                ('tweet_media', models.TextField()),
                ('tweet_gpt', models.TextField()),
                ('alpha_time', models.TextField()),
            ],
        ),
    ]