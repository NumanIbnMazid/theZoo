from util.helpers import simple_form_widget, validate_chars
from .models import (
    Species, HealthPoint, Animal, AnimalCage
)
from django import forms
import datetime



class SpeciesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpeciesForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter species name...'
        )
        simple_form_widget(
            self=self, field='kingdom', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter kingdom...'
        )
        simple_form_widget(
            self=self, field='phylum', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter phylum...'
        )
        simple_form_widget(
            self=self, field='class_name', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter class name...'
        )
        simple_form_widget(
            self=self, field='order', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter order...'
        )
        simple_form_widget(
            self=self, field='family', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter family...'
        )
        simple_form_widget(
            self=self, field='genus', maxlength=100, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter genus...'
        )

    class Meta:
        model = Species
        fields = [
            'name', 'kingdom', 'phylum', 'class_name', 'order', 'family', 'genus'
        ]


class HealthPointForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HealthPointForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter equipment name...'
        )
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )

    class Meta:
        model = HealthPoint
        fields = [
            'name', 'description'
        ]


class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter animal name...'
        )
        simple_form_widget(
            self=self, field='colour', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter colour...'
        )
        simple_form_widget(
            self=self, field='weight', step=00.01, pattern="^[0-9.]{1,}$", 
            placeholder='Enter weight (in kg)...'
        )
        self.fields['dob'].widget.attrs.update({
            'id': 'datetimepicker_DOB',
            'autocomplete': 'off',
            'placeholder': "Select date of birth..."
        })
    class Meta:
        model = Animal
        fields = [
            'name', 'species', 'animal_type', 'colour', 'weight', 'dob', 'country',
            'image', 'health_point', #'cage'
        ]

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if not dob == None:
            today = datetime.date.today()
            if dob > today:
                raise forms.ValidationError(
                    "Please enter valid Date of Birth. Date cannot be greater than today!")
        return dob


class AnimalCageForm(forms.ModelForm):
    class Meta:
        model = AnimalCage
        fields = [
            'cage', 'animal'
        ]