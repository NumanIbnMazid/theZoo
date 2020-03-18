from django.contrib import admin
from util.mixins import CustomModelAdminMixin
from .models import Food, AnimalFood


class FoodAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Food


admin.site.register(Food, FoodAdmin)


class AnimalFoodAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = AnimalFood


admin.site.register(AnimalFood, AnimalFoodAdmin)
