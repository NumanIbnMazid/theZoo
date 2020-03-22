# Generated by Django 3.0.4 on 2020-03-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_auto_20200322_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentset',
            name='equipments',
        ),
        migrations.AddField(
            model_name='equipmentset',
            name='equipments',
            field=models.ManyToManyField(related_name='equipment_set_equipment', to='maintenance.Equipment', verbose_name='Equipments'),
        ),
    ]