from django.db import models
from animal.models import Animal

class Food(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    description = models.TextField(
        max_length=500, verbose_name='Description', null=True, blank=True
    )
    protein = models.IntegerField(
        verbose_name='Protein', null=True, blank=True
    )
    carbohydrate = models.IntegerField(
        verbose_name='Carbohydrate', null=True, blank=True
    )
    fat = models.IntegerField(
        verbose_name='Fat', null=True, blank=True
    )
    vitamin = models.IntegerField(
        verbose_name='Vitamin', null=True, blank=True
    )
    mineral = models.IntegerField(
        verbose_name='Mineral', null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
        ordering = ['-created_at']


class AnimalFood(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal_food_animal', verbose_name='Animal'
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='animal_food_food', verbose_name='Food'
    )
    date = models.DateField(
        verbose_name='Date', null=True, blank=True
    )
    quantity = models.IntegerField(
        verbose_name='Quantity', null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.animal.name

    class Meta:
        verbose_name = 'Animal Food'
        verbose_name_plural = 'Animal Foods'
        ordering = ['-created_at']
