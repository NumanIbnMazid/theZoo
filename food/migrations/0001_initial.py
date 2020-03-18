# Generated by Django 3.0.4 on 2020-03-18 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('protein', models.IntegerField(blank=True, null=True, verbose_name='Protein')),
                ('carbohydrate', models.IntegerField(blank=True, null=True, verbose_name='Carbohydrate')),
                ('fat', models.IntegerField(blank=True, null=True, verbose_name='Fat')),
                ('vitamin', models.IntegerField(blank=True, null=True, verbose_name='Vitamin')),
                ('mineral', models.IntegerField(blank=True, null=True, verbose_name='Mineral')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AnimalFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_food_animal', to='animal.Animal', verbose_name='Animal')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_food_food', to='food.Food', verbose_name='Food')),
            ],
            options={
                'verbose_name': 'Animal Food',
                'verbose_name_plural': 'Animal Foods',
                'ordering': ['-created_at'],
            },
        ),
    ]
