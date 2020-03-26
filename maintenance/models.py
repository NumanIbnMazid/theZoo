from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime
from staff.models import Staff
from util.helpers import get_dynamic_fields



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
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
        ordering = ['-created_at']


class EquipmentSet(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    equipments = models.ManyToManyField(
        Equipment, related_name='equipment_set_equipment', verbose_name='Equipments'
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
        values = ','.join([str(elem)
                          for elem in self.equipments.all()])
        return self.name + f" [{values}]"

    class Meta:
        verbose_name = 'Equipment Set'
        verbose_name_plural = 'Equipment Sets'
        ordering = ['-created_at']


    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'equipments':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.equipments.all()])
                else:
                    value = self.equipments.name
                return (field.name, value)
            elif field.name == 'x':
                return (field.name, self.x.title)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]
    


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
        )], null=True, blank=True, verbose_name='Length (feet)'
    )
    height = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Height (feet)'
    )
    width = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(
            Decimal(0.00)
        )], null=True, blank=True, verbose_name='Width (feet)'
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

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


class Maintenance(models.Model):
    cage = models.ForeignKey(
        Cage, on_delete=models.CASCADE, related_name='cage_maintenance', verbose_name='Cage'
    )
    staff = models.ManyToManyField(
        Staff, related_name='staff_maintenance', verbose_name='Staff'
    )
    date = models.DateField(
        verbose_name='Date'
    )
    start_time = models.DateTimeField(
        verbose_name='Start Time'
    )
    end_time = models.DateTimeField(
        verbose_name='End Time'
    )
    equipment_set = models.ManyToManyField(
        EquipmentSet, related_name='maintenence_equipment_set', verbose_name='Equipment Set'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.cage.name

    class Meta:
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenances'
        ordering = ['date']

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'staff':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.staff.all()])
                else:
                    value = self.staff.name
                return (field.name, value)
            elif field.name == 'equipment_set':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.equipment_set.all()])
                else:
                    value = self.equipment_set.name
                return (field.name, value)
            elif field.name == 'cage':
                return (field.name, self.cage.name)
            elif field.name == 'x':
                return (field.name, self.x.title)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]


class Incident(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Title'
    )
    staff = models.ManyToManyField(
        Staff, related_name='staff_incident', verbose_name='Staff'
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

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'staff':
                if field.get_internal_type() == 'ManyToManyField':
                    value = ','.join([str(elem)
                                      for elem in self.staff.all()])
                else:
                    value = self.staff.name
                return (field.name, value)
            elif field.name == 'cage':
                return (field.name, self.cage.name)
            elif field.name == 'x':
                return (field.name, self.x.title)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]



# Employee Slug Generate
# def maintenance_date_pre_save_reciever(sender, instance, *args, **kwargs):
#     str_date = str(instance.date).split('-')
#     str_start_time = str(instance.start_time).split(':')
#     str_end_time = str(instance.end_time).split(':')
#     start_date = datetime.datetime(
#         int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
#             str_start_time[0]), int(str_start_time[1])
#     )
#     end_date = datetime.datetime(
#         int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
#             str_end_time[0]), int(str_end_time[1])
#     )
#     instance.start_time = start_date
#     instance.end_time = end_date
#     print("ZZZZ")


# pre_save.connect(maintenance_date_pre_save_reciever, sender=Maintenance)
