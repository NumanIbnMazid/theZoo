from django.urls import path
from .views import (
    EquipmentCreateView, EquipmentUpdateView, delete_equipment
)


urlpatterns = [
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
]
