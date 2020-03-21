from util.helpers import simple_form_widget, validate_chars
from .models import (
    Equipment, EquipmentSet, Cage, Maintenance, Incident
)
from django import forms


class EquipmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9 .,'-#]{1,}$",
            placeholder='Enter equipment name...'
        )
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )

    class Meta:
        model = Equipment
        fields = [
            'name', 'description'
        ]
