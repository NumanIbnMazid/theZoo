# Generated by Django 3.0.4 on 2020-05-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_animaltreatment_recovered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaltreatment',
            name='recovered',
            field=models.CharField(choices=[('Recovered', 'Recovered'), ('Not Recovered', 'Not Recovered')], default='No', max_length=50, verbose_name='Recovered'),
        ),
    ]
