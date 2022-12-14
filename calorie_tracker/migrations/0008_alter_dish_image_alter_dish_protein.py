# Generated by Django 4.1.3 on 2022-11-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_tracker', '0007_alter_dish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='calorie_tracker/photos/'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='protein',
            field=models.IntegerField(),
        ),
    ]
