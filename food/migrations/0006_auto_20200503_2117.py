# Generated by Django 3.0.4 on 2020-05-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20200327_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalfood',
            name='food',
        ),
        migrations.AddField(
            model_name='animalfood',
            name='food',
            field=models.ManyToManyField(related_name='animal_food_food', to='food.Food', verbose_name='Food'),
        ),
    ]
