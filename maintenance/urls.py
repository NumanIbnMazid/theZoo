from django.urls import path
from .views import (
    EquipmentCreateView, EquipmentUpdateView, delete_equipment,
    EquipmentSetCreateView, EquipmentSetUpdateView, delete_equipment_set,
    CageCreateView, CageUpdateView, delete_cage,
    MaintenanceCreateView, MaintenanceUpdateView, delete_maintenance,
)


urlpatterns = [
    # Equipment
    path(
        'add-equipment/', EquipmentCreateView.as_view(),
        name='add_equipment'
    ),
    path(
        'update-equipment/<id>', EquipmentUpdateView.as_view(),
        name='update_equipment'
    ),
    path(
        'delete-equipment/', delete_equipment,
        name='delete_equipment'
    ),
    # Equipment Set
    path(
        'add-equipment-set/', EquipmentSetCreateView.as_view(),
        name='add_equipment_set'
    ),
    path(
        'update-equipment-set/<id>', EquipmentSetUpdateView.as_view(),
        name='update_equipment_set'
    ),
    path(
        'delete-equipment-set/', delete_equipment_set,
        name='delete_equipment_set'
    ),
    # Cage
    path(
        'add-cage/', CageCreateView.as_view(),
        name='add_cage'
    ),
    path(
        'update-cage/<id>', CageUpdateView.as_view(),
        name='update_cage'
    ),
    path(
        'delete-cage/', delete_cage,
        name='delete_cage'
    ),
    # Maintenance
    path(
        'add-maintenance/', MaintenanceCreateView.as_view(),
        name='add_maintenance'
    ),
    path(
        'update-maintenance/<id>', MaintenanceUpdateView.as_view(),
        name='update_maintenance'
    ),
    path(
        'delete-maintenance/', delete_maintenance,
        name='delete_maintenance'
    ),
]
