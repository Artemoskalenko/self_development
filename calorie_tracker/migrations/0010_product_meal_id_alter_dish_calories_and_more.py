# Generated by Django 4.1.3 on 2022-11-06 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_tracker', '0009_alter_dish_calories_alter_dish_protein'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meal_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='calorie_tracker.meal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='calories',
            field=models.IntegerField(verbose_name='Калории'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='carbohydrates',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='fat',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='calorie_tracker/photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название блюда'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='protein',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Белки'),
        ),
    ]