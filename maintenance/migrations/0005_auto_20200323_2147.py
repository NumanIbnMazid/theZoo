# Generated by Django 3.0.4 on 2020-03-23 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_auto_20200323_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date'], 'verbose_name': 'Maintenance', 'verbose_name_plural': 'Maintenances'},
        ),
    ]