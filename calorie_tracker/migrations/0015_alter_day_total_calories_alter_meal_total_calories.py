# Generated by Django 4.1.3 on 2022-11-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_tracker', '0014_product_calories_alter_day_total_calories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='total_calories',
            field=models.IntegerField(default=0, verbose_name='Калории'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='total_calories',
            field=models.IntegerField(default=0, verbose_name='Калории'),
        ),
    ]
