# Generated by Django 3.0.4 on 2020-05-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_auto_20200327_0507'),
        ('animal', '0005_auto_20200503_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalCage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_cage', to='animal.Animal', verbose_name='Animal')),
                ('cage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cage_animal', to='maintenance.Cage', verbose_name='Cage')),
            ],
            options={
                'verbose_name': 'Animal Cage',
                'verbose_name_plural': 'Animal Cages',
                'ordering': ['-created_at'],
            },
        ),
    ]