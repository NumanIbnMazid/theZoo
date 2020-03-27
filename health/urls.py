from django.urls import path
from .views import (
    MedicineCreateView, MedicineUpdateView, delete_medicine,
    DiseaseCreateView, DiseaseUpdateView, delete_disease,
    AnimalTreatmentCreateView, AnimalTreatmentUpdateView, delete_animal_treatment,
)


urlpatterns = [
    # Medicine
    path(
        'add-medicine/', MedicineCreateView.as_view(),
        name='add_medicine'
    ),
    path(
        'update-medicine/<id>', MedicineUpdateView.as_view(),
        name='update_medicine'
    ),
    path(
        'delete-medicine/', delete_medicine,
        name='delete_medicine'
    ),
    # Disease
    path(
        'add-disease/', DiseaseCreateView.as_view(),
        name='add_disease'
    ),
    path(
        'update-disease/<id>', DiseaseUpdateView.as_view(),
        name='update_disease'
    ),
    path(
        'delete-disease/', delete_disease,
        name='delete_disease'
    ),
    # AnimalTreatment
    path(
        'add-animal-treatment/', AnimalTreatmentCreateView.as_view(),
        name='add_animal_treatment'
    ),
    path(
        'update-animal-treatment/<id>', AnimalTreatmentUpdateView.as_view(),
        name='update_animal_treatment'
    ),
    path(
        'delete-animal-treatment/', delete_animal_treatment,
        name='delete_animal_treatment'
    ),
]
