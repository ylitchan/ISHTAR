# Generated by Django 4.1.3 on 2022-12-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myAPP", "0007_rename_zf_stocks_changeratio_rename_dm_stocks_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="stocks",
            name="ths_up_and_down_status_stock",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
