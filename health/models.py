from django.db import models
from django_countries.fields import CountryField
from animal.models import Animal
from staff.models import Staff


class Medicine(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    manufacturer = models.CharField(
        max_length=100, verbose_name='Manufacturer'
    )
    country = CountryField(blank=True, null=True)
    composition = models.CharField(
        max_length=100, verbose_name='Composition'
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
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'
        ordering = ['-created_at']


class Disease(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal_disease', verbose_name='Animal'
    )
    date = models.DateField(
        verbose_name='Date', null=True, blank=True
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
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'
        ordering = ['-created_at']


class AnimalTreatment(models.Model):
    # animal = models.ForeignKey(
    #     Animal, on_delete=models.CASCADE, related_name='animal_treatment', verbose_name='Animal'
    # )
    disease = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, related_name='animal_treatment_disease', verbose_name='Disease'
    )
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, related_name='animal_treatment_medicine', verbose_name='Medicine'
    )
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='animal_treatment_staff', verbose_name='Staff'
    )
    date = models.DateField(
        verbose_name='Date', null=True, blank=True
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
        return self.animal.name

    class Meta:
        verbose_name = 'AnimalTreatment'
        verbose_name_plural = 'AnimalTreatments'
        ordering = ['-created_at']
