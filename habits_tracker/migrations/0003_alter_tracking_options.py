# Generated by Django 4.1 on 2022-08-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0002_alter_habits_options_alter_tracking_day_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracking',
            options={'ordering': ['day'], 'verbose_name': 'Трэкинг', 'verbose_name_plural': 'Трэкинг'},
        ),
    ]
