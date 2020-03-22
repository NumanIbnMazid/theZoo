from django.urls import path
from .views import (
    EquipmentCreateView, EquipmentUpdateView, delete_equipment,
    EquipmentSetCreateView, EquipmentSetUpdateView, delete_equipment_set,
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
]
