from django.db import models
from animal.models import Animal
from util.helpers import get_dynamic_fields
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db.models import Q


class FoodQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (Q(name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(protein__icontains=query) |
                   Q(carbohydrate__icontains=query) |
                   Q(fat__icontains=query) |
                   Q(vitamin__icontains=query) |
                   Q(mineral__icontains=query)
                   )
        return self.filter(lookups).distinct()


class FoodManager(models.Manager):
    def get_queryset(self):
        return FoodQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)

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
        )], null=True, blank=True, verbose_name='Protein'
    )
    carbohydrate = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Carbohydrate'
    )
    fat = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Fat'
    )
    vitamin = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Vitamin'
    )
    mineral = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Mineral'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    objects = FoodManager()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
        ordering = ['-created_at']


class AnimalFoodQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (Q(animal__name__icontains=query) |
                   Q(animal__slug__icontains=query) |
                   Q(animal__species__name__icontains=query) |
                   Q(animal__animal_type__icontains=query) |
                   Q(animal__colour__icontains=query) |
                   Q(animal__weight__icontains=query) |
                   Q(animal__dob__icontains=query) |
                   Q(animal__country__icontains=query) |
                   Q(animal__health_point__name__icontains=query) |
                   Q(food__name__icontains=query) |
                   Q(food__description__icontains=query) |
                   Q(food__protein__icontains=query) |
                   Q(food__carbohydrate__icontains=query) |
                   Q(food__fat__icontains=query) |
                   Q(food__vitamin__icontains=query) |
                   Q(food__mineral__icontains=query)
                   )
        return self.filter(lookups).distinct()


class AnimalFoodManager(models.Manager):
    def get_queryset(self):
        return AnimalFoodQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)

class AnimalFood(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal_food_animal', verbose_name='Animal'
    )
    food = models.ManyToManyField(
        Food, related_name='animal_food_food', verbose_name='Food'
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

    objects = AnimalFoodManager()

    def __str__(self):
        return self.animal.name

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'animal':
                return (field.name, self.animal.get_name)
            elif field.name == 'food':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.food.all()])
                else:
                    value = self.food.name
                return (field.name, value)
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
