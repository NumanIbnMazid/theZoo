from .models import Food, AnimalFood
from util.helpers import simple_form_widget, validate_chars
from django import forms
import datetime


class FoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter food name...'
        )
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )
        self.fields['protein'].help_text = "% per Kilogram (1000 gram)"
        self.fields['carbohydrate'].help_text = "% per Kilogram (1000 gram)"
        self.fields['fat'].help_text = "% per Kilogram (1000 gram)"
        self.fields['vitamin'].help_text = "% per Kilogram (1000 gram)"
        self.fields['mineral'].help_text = "% per Kilogram (1000 gram)"

    class Meta:
        model = Food
        fields = [
            'name', 'protein', 'carbohydrate', 'fat', 'vitamin', 'mineral', 'description'
        ]


class AnimalFoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnimalFoodForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'id': 'datepicker1',
            'autocomplete': 'off'
        })

    class Meta:
        model = AnimalFood
        fields = [
            'animal', 'food', 'date', 'quantity'
        ]
