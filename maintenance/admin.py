from django.contrib import admin
from util.mixins import CustomModelAdminMixin
from .models import (
    Equipment, EquipmentSet, Cage, Maintenance, Incident
)


class EquipmentAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Equipment


admin.site.register(Equipment, EquipmentAdmin)


class EquipmentSetAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = EquipmentSet


admin.site.register(EquipmentSet, EquipmentSetAdmin)


class CageAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Cage


admin.site.register(Cage, CageAdmin)


class MaintenanceAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Maintenance


admin.site.register(Maintenance, MaintenanceAdmin)


class IncidentAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Incident


admin.site.register(Incident, IncidentAdmin)
