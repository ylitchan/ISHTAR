# Generated by Django 4.1.7 on 2023-03-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_payorder_express_address_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorder',
            name='express_info',
            field=models.IntegerField(default=1),
        ),
    ]
