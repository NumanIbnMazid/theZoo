# Generated by Django 3.0.4 on 2020-05-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_animal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='UID'),
        ),
    ]