from django.contrib import admin
from util.mixins import CustomModelAdminMixin
from .models import (
    Species, HealthPoint, Animal, AnimalCage
)


class SpeciesAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Species


admin.site.register(Species, SpeciesAdmin)


class HealthPointAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = HealthPoint


admin.site.register(HealthPoint, HealthPointAdmin)


class AnimalAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Animal


admin.site.register(Animal, AnimalAdmin)


class AnimalCageAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = AnimalCage


admin.site.register(AnimalCage, AnimalCageAdmin)
