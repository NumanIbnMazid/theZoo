from django.db import models
from .utils import upload_image_path
from django.core.validators import MinValueValidator
from decimal import Decimal
from django_countries.fields import CountryField
from maintenance.models import Cage



class Species(models.Model):
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
        )], null=True, blank=True, verbose_name='Weight'
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

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
        ordering = ['-created_at']

