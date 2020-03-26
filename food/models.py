from django.db import models
from animal.models import Animal
from util.helpers import get_dynamic_fields
from django.core.validators import MinValueValidator
from decimal import Decimal

class Food(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    description = models.TextField(
        max_length=500, verbose_name='Description', null=True, blank=True
    )
    protein = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Protein (gm)'
    )
    carbohydrate = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Carbohydrate (gm)'
    )
    fat = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Fat (gm)'
    )
    vitamin = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Vitamin (gm)'
    )
    mineral = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Mineral (gm)'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.name

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]

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
    quantity = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Quantity (kg)'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.animal.name

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'animal':
                return (field.name, self.animal.name)
            elif field.name == 'food':
                return (field.name, self.food.name)
            elif field.name == 'x':
                return (field.name, self.x.title)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]

    class Meta:
        verbose_name = 'Animal Food'
        verbose_name_plural = 'Animal Foods'
        ordering = ['-created_at']
