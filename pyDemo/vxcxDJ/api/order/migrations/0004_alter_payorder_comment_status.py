# Generated by Django 4.1.7 on 2023-03-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_payorder_express_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorder',
            name='comment_status',
            field=models.IntegerField(default=1),
        ),
    ]
