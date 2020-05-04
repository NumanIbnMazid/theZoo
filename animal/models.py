from django.db import models
from .utils import upload_image_path
from django.core.validators import MinValueValidator
from decimal import Decimal
from django_countries.fields import CountryField
from maintenance.models import Cage
from util.helpers import get_dynamic_fields
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from util.utils import unique_slug_generator, random_number_generator
from django.db.models import Q


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


class AnimalQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (Q(name__icontains=query) |
                   Q(slug__icontains=query) |
                   Q(species__name__icontains=query) |
                   Q(animal_type__icontains=query) |
                   Q(colour__icontains=query) |
                   Q(weight__icontains=query) |
                   Q(dob__icontains=query) |
                   Q(country__icontains=query) |
                   Q(health_point__name__icontains=query)
                   )
        return self.filter(lookups).distinct()


class AnimalManager(models.Manager):
    def get_queryset(self):
        return AnimalQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)

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
    slug = models.SlugField(unique=True, max_length=255, verbose_name='UID')
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
    # cage = models.ForeignKey(
    #     Cage, on_delete=models.CASCADE, related_name='animal_cage', verbose_name='Cage'
    # )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    objects = AnimalManager()

    def __str__(self):
        return self.name + f" [{self.slug}]"

    def get_name(self):
        return self.name + f" [{self.slug}]"

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


class AnimalCageQuerySet(models.query.QuerySet):
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
                   Q(cage__name__icontains=query) |
                   Q(cage__length__icontains=query) |
                   Q(cage__height__icontains=query) |
                   Q(cage__width__icontains=query) |
                   Q(cage__cover_type__icontains=query)
                   )
        return self.filter(lookups).distinct()


class AnimalCageManager(models.Manager):
    def get_queryset(self):
        return AnimalCageQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)

class AnimalCage(models.Model):
    cage = models.ForeignKey(
        Cage, on_delete=models.CASCADE, related_name='cage_animal', verbose_name='Cage'
    )
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal_cage', verbose_name='Animal'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    objects = AnimalCageManager()

    def __str__(self):
        return self.cage.name

    def get_cage(self):
        qs_count = AnimalCage.objects.filter(cage=self.cage).count()
        return (self.cage.name + f" [Animals: {qs_count}]")
    
    def get_animals(self):
        animals = []
        for animal_cage in AnimalCage.objects.filter(cage=self.cage):
            animals.append(animal_cage.animal.get_name())
        return animals

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'cage':
                qs_count = AnimalCage.objects.filter(cage=self.cage).count()
                return (field.name, self.get_cage)
            elif field.name == 'animal':
                return (field.name, self.animal.name + f" [{self.animal.slug}]")
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]

    class Meta:
        verbose_name = 'Animal Cage'
        verbose_name_plural = 'Animal Cages'
        ordering = ['-created_at']


# Branch Category Slug Generator with pre save
def animal_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    '''
    DOCSTRING for animal_slug_pre_save_receiver():
    This method generates slug before saving the object.
    If slug already exists that will be remain unaltered.
    If not exists then this method will automatically save slug before saving the object.
    '''
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.name) + "-" + random_number_generator()


pre_save.connect(animal_slug_pre_save_receiver, sender=Animal)


# @receiver(post_save, sender=Animal)
# def create_animal_cage(sender, instance, created, **kwargs):
#     if created:
#         AnimalCage.objects.create(animal=instance, cage=instance.cage)
