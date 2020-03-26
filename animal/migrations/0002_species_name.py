# Generated by Django 3.0.4 on 2020-03-25 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]