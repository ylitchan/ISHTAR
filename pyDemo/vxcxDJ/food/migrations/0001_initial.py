# Generated by Django 4.1.7 on 2023-03-02 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.IntegerField()),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('main_image', models.TextField()),
                ('summary', models.TextField()),
                ('stock', models.IntegerField()),
                ('tags', models.TextField()),
                ('status', models.IntegerField()),
                ('month_count', models.IntegerField(default=0)),
                ('total_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('weight', models.IntegerField()),
                ('status', models.IntegerField()),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodSaleChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('member_id', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodStockChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('total_stock', models.IntegerField()),
                ('note', models.TextField()),
            ],
        ),
    ]
