from util.helpers import simple_form_widget, validate_chars
from .models import (
    Medicine, Disease, AnimalTreatment
)
from django import forms
import datetime



class MedicineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter medicine name...'
        )
        simple_form_widget(
            self=self, field='manufacturer', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter manufacturer name...'
        )
        simple_form_widget(
            self=self, field='composition', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter composition name...'
        )
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )

    class Meta:
        model = Medicine
        fields = [
            'name', 'manufacturer', 'country', 'composition', 'description'
        ]


class DiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiseaseForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9.,# ]{1,}$",
            placeholder='Enter disease name...'
        )
        self.fields['date'].widget.attrs.update({
            'id': 'datepicker2',
            'autocomplete': 'off'
        })
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )

    class Meta:
        model = Disease
        fields = [
            'name', 'animal', 'date', 'description'
        ]

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date == None:
            today = datetime.date.today()
            if not date <= today:
                raise forms.ValidationError(
                    'Date must be smaller than or equal today!')
            return date
        return None


class AnimalTreatmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnimalTreatmentForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'id': 'datepicker2',
            'autocomplete': 'off'
        })
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )

    class Meta:
        model = AnimalTreatment
        fields = [
            'disease', 'medicine', 'staff', 'date', 'description'
        ]

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date == None:
            today = datetime.date.today()
            if not date <= today:
                raise forms.ValidationError(
                    'Date must be smaller than or equal today!')
            return date
        return None
