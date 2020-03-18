from django.contrib import admin
from util.mixins import CustomModelAdminMixin
from .models import (
    Medicine, Disease, AnimalTreatment
)


class MedicineAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Medicine


admin.site.register(Medicine, MedicineAdmin)


class DiseaseAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Disease


admin.site.register(Disease, DiseaseAdmin)


class AnimalTreatmentAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = AnimalTreatment


admin.site.register(AnimalTreatment, AnimalTreatmentAdmin)
