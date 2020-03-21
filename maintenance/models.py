from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from staff.models import Staff



class Equipment(models.Model):
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
        def get_dynamic_fields(field):
            if field.name == 'x':
                return (field.name, self.x.title)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
        ordering = ['-created_at']


class EquipmentSet(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    equipments = models.CharField(
        max_length=255, verbose_name='Equipments'
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
        verbose_name = 'Equipment Set'
        verbose_name_plural = 'Equipment Sets'
        ordering = ['-created_at']



class Cage(models.Model):
    GLASS = 'Glass'
    REPTILE = 'Reptile'
    COVER_TYPE_CHOICES = (
        (GLASS, 'Glass'),
        (REPTILE, 'Reptile'),
    )

    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    length = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Length'
    )
    height = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Height'
    )
    width = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Width'
    )
    cover_type = models.CharField(
        max_length=100, choices=COVER_TYPE_CHOICES, verbose_name='Cover Type'
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
        verbose_name = 'Cage'
        verbose_name_plural = 'Cages'
        ordering = ['-created_at']


class Maintenance(models.Model):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='staff_maintenance', verbose_name='Staff'
    )
    cage = models.ForeignKey(
        Cage, on_delete=models.CASCADE, related_name='cage_maintenance', verbose_name='Cage'
    )
    date = models.DateField(
        verbose_name='Date'
    )
    start_time = models.TimeField(
        verbose_name='Start Time'
    )
    end_time = models.TimeField(
        verbose_name='End Time'
    )
    equipment_set = models.ForeignKey(
        EquipmentSet, on_delete=models.CASCADE, related_name='maintenence_equipment_set', verbose_name='Equipment Set'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.staff.name

    class Meta:
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenances'
        ordering = ['-created_at']


class Incident(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Title'
    )
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='staff_incident', verbose_name='Staff'
    )
    cage = models.ForeignKey(
        Cage, on_delete=models.CASCADE, related_name='cage_incident', verbose_name='Cage'
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
        return self.title

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'
        ordering = ['-created_at']
