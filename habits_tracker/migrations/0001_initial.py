# Generated by Django 4.1.3 on 2022-11-04 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('qr', models.ImageField(upload_to='qr_images')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Завершено')),
                ('day', models.DateField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits_tracker.habits')),
            ],
            options={
                'verbose_name': 'Трэкинг',
                'verbose_name_plural': 'Трэкинг',
                'ordering': ['day'],
            },
        ),
    ]
