# Generated by Django 3.0.4 on 2020-05-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20200327_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaltreatment',
            name='recovered',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=50, verbose_name='Recovered'),
        ),
    ]
