# Generated by Django 4.1.3 on 2022-12-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myAPP", "0003_remove_article_article_abstract_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="article_abstract",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
