from django.db import models
from django_countries.fields import CountryField
from animal.models import Animal
from staff.models import Staff
from util.helpers import get_dynamic_fields
from django.db.models import Q

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

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'
        ordering = ['-created_at']


class DiseaseQuerySet(models.query.QuerySet):
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
                   Q(name__icontains=query) |
                   Q(date__icontains=query) |
                   Q(description__icontains=query)
                   )
        return self.filter(lookups).distinct()


class DiseaseManager(models.Manager):
    def get_queryset(self):
        return DiseaseQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)

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

    objects = DiseaseManager()

    def __str__(self):
        return self.name + f" [{self.animal.name}]"

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'animal':
                return (field.name, self.animal.get_name)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]

    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'
        ordering = ['-created_at']


class AnimalTreatmentQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (Q(disease__animal__name__icontains=query) |
                   Q(disease__animal__slug__icontains=query) |
                   Q(disease__animal__species__name__icontains=query) |
                   Q(disease__animal__animal_type__icontains=query) |
                   Q(disease__animal__colour__icontains=query) |
                   Q(disease__animal__weight__icontains=query) |
                   Q(disease__animal__dob__icontains=query) |
                   Q(disease__animal__country__icontains=query) |
                   Q(disease__animal__health_point__name__icontains=query) |
                   Q(disease__name__icontains=query) |
                   Q(disease__date__icontains=query) |
                   Q(disease__description__icontains=query) |
                   Q(staff__user__username__icontains=query) |
                   Q(staff__user__first_name__icontains=query) |
                   Q(staff__user__last_name__icontains=query) |
                   Q(staff__role__icontains=query) |
                   Q(staff__gender__icontains=query) |
                   Q(staff__dob__icontains=query) |
                   Q(staff__address__icontains=query) |
                   Q(staff__phone__icontains=query) |
                   Q(staff__posting__icontains=query) |
                   Q(staff__insurance_cover__icontains=query) |
                   Q(date__icontains=query) |
                   Q(description__icontains=query) |
                   Q(recovered__icontains=query)
                   )
        return self.filter(lookups).distinct()


class AnimalTreatmentManager(models.Manager):
    def get_queryset(self):
        return AnimalTreatmentQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)


class AnimalTreatment(models.Model):
    # CONDITION_CHOICES
    YES = 'Recovered'
    NO = 'Not Recovered'
    CONDITION_CHOICES = (
        (YES, 'Recovered'),
        (NO, 'Not Recovered'),
    )
    # animal = models.ForeignKey(
    #     Animal, on_delete=models.CASCADE, related_name='animal_treatment', verbose_name='Animal'
    # )
    disease = models.ForeignKey(
        Disease, on_delete=models.CASCADE, related_name='animal_treatment_disease', verbose_name='Disease'
    )
    medicine = models.ManyToManyField(
        Medicine, related_name='animal_treatment_medicine', verbose_name='Medicine'
    )
    staff = models.ManyToManyField(
        Staff, related_name='animal_treatment_staff', verbose_name='Staff'
    )
    date = models.DateField(
        verbose_name='Date', null=True, blank=True
    )
    description = models.TextField(
        max_length=500, null=True, blank=True, verbose_name='Description'
    )
    recovered = models.CharField(
        default='Not Recovered', choices=CONDITION_CHOICES, max_length=50, verbose_name='Recovered'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    objects = AnimalTreatmentManager()

    def __str__(self):
        return self.animal.name

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'medicine':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.medicine.all()])
                else:
                    value = self.medicine.name
                return (field.name, value)
            elif field.name == 'staff':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.staff.all()])
                else:
                    value = self.staff.name
                return (field.name, value)
            elif field.name == 'disease':
                return (field.name, self.disease)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]

    class Meta:
        verbose_name = 'AnimalTreatment'
        verbose_name_plural = 'AnimalTreatments'
        ordering = ['-created_at']
