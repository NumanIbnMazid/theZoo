from django.db import models
from .utils import upload_image_path
from django.core.validators import MinValueValidator
from decimal import Decimal
from django_countries.fields import CountryField
from maintenance.models import Cage
from util.helpers import get_dynamic_fields



class Species(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    kingdom = models.CharField(
        max_length=100, verbose_name='Kingdom'
    )
    phylum = models.CharField(
        max_length=100, verbose_name='Phylum'
    )
    class_name = models.CharField(
        max_length=100, verbose_name='Class Name'
    )
    order = models.CharField(
        max_length=100, verbose_name='Order'
    )
    family = models.CharField(
        max_length=100, verbose_name='Family'
    )
    genus = models.CharField(
        max_length=100, verbose_name='Genus'
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
        verbose_name = 'Species'
        verbose_name_plural = 'Specieses'
        ordering = ['-created_at']


class HealthPoint(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    description = models.TextField(
        max_length=500, null=True, blank=True, verbose_name='Description'
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
        verbose_name = 'HealthPoint'
        verbose_name_plural = 'HealthPoints'
        ordering = ['-created_at']


class Animal(models.Model):
    INVERTEBRATES = 'Invertebrates'
    FISH = 'Fish'
    AMPHIBIANS = 'Amphibians'
    REPTILES = 'Reptiles'
    BIRDS = 'Birds'
    MAMMALS = 'Mammals'
    ANIMAL_TYPE_CHOICES = (
        (INVERTEBRATES, 'Invertebrates'),
        (FISH, 'Fish'),
        (AMPHIBIANS, 'Amphibians'),
        (REPTILES, 'Reptiles'),
        (BIRDS, 'BIRDS'),
        (MAMMALS, 'Mammals'),
    )
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    species = models.ForeignKey(
        Species, on_delete=models.CASCADE, related_name='animal_species', verbose_name='Species'
    )
    animal_type = models.CharField(
        max_length=100, choices=ANIMAL_TYPE_CHOICES, verbose_name='Animal Type'
    )
    colour = models.CharField(
        max_length=100, verbose_name='Colour'
    )
    weight = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Weight (kg)'
    )
    dob = models.DateField(
        null=True, blank=True, verbose_name='DOB'
    )
    country = CountryField(blank=True, null=True)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True, verbose_name='Image'
    )
    health_point = models.ForeignKey(
        HealthPoint, on_delete=models.CASCADE, related_name='animal_health_point', verbose_name='Health Point'
    )
    cage = models.ForeignKey(
        Cage, on_delete=models.CASCADE, related_name='animal_cage', verbose_name='Cage'
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
        def get_dynamic_fields(field):
            if field.name == 'species':
                return (field.name, self.species.name)
            elif field.name == 'health_point':
                return (field.name, self.health_point.name)
            elif field.name == 'cage':
                return (field.name, self.cage.name)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
        ordering = ['-created_at']

