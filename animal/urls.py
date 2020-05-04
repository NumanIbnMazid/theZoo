from django.urls import path
from .views import (
    SpeciesCreateView, SpeciesUpdateView, delete_species,
    HealthPointCreateView, HealthPointUpdateView, delete_health_point,
    AnimalCreateView, AnimalUpdateView, delete_animal,
    AnimalCageCreateView, AnimalCageUpdateView, delete_animal_cage,
)


urlpatterns = [
    # Species
    path(
        'add-species/', SpeciesCreateView.as_view(),
        name='add_species'
    ),
    path(
        'update-species/<id>', SpeciesUpdateView.as_view(),
        name='update_species'
    ),
    path(
        'delete-species/', delete_species,
        name='delete_species'
    ),
    # HealthPoint
    path(
        'add-health-point/', HealthPointCreateView.as_view(),
        name='add_health_point'
    ),
    path(
        'update-health-point/<id>', HealthPointUpdateView.as_view(),
        name='update_health_point'
    ),
    path(
        'delete-health-point/', delete_health_point,
        name='delete_health_point'
    ),
    # Animal
    path(
        'add-animal/', AnimalCreateView.as_view(),
        name='add_animal'
    ),
    path(
        'update-animal/<id>', AnimalUpdateView.as_view(),
        name='update_animal'
    ),
    path(
        'delete-animal/', delete_animal,
        name='delete_animal'
    ),
    # AnimalCage
    path(
        'add-animal-cage/', AnimalCageCreateView.as_view(),
        name='add_animal_cage'
    ),
    path(
        'update-animal-cage/<id>', AnimalCageUpdateView.as_view(),
        name='update_animal_cage'
    ),
    path(
        'delete-animal-cage/', delete_animal_cage,
        name='delete_animal_cage'
    ),
]
