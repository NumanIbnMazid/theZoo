from django.urls import path
from .views import (
    FoodCreateView, FoodUpdateView, delete_food,
    AnimalFoodCreateView, AnimalFoodUpdateView, delete_animal_food,
)


urlpatterns = [
    # Food
    path(
        'add-food/', FoodCreateView.as_view(),
        name='add_food'
    ),
    path(
        'update-food/<id>', FoodUpdateView.as_view(),
        name='update_food'
    ),
    path(
        'delete-food/', delete_food,
        name='delete_food'
    ),
    # AnimalFood
    path(
        'add-animal-food/', AnimalFoodCreateView.as_view(),
        name='add_animal_food'
    ),
    path(
        'update-animal-food/<id>', AnimalFoodUpdateView.as_view(),
        name='update_animal_food'
    ),
    path(
        'delete-animal-food/', delete_animal_food,
        name='delete_animal_food'
    ),
]
