from util.helpers import simple_form_widget, validate_chars
from .models import (
    Equipment, EquipmentSet, Cage, Maintenance, Incident
)
from util.fields import GroupedModelChoiceField
from django import forms
import datetime


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


class EquipmentSetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentSetForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9 .,'-#]{1,}$",
            placeholder='Enter equipment name...'
        )
        self.fields['equipments'] = forms.ModelMultipleChoiceField(
            queryset=Equipment.objects.all()
        )
        # self.fields['equipments'] = GroupedModelChoiceField(
        #     queryset=Category.objects.exclude(parent=None),
        #     choices_groupby='parent'
        # )
        self.fields['equipments'].help_text = "Hold down “Control”, or “Command” on a Mac, to select more than one."
        simple_form_widget(
            self=self, field='description', placeholder='Enter description...'
        )

    class Meta:
        model = EquipmentSet
        fields = [
            'name', 'equipments', 'description'
        ]


class CageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CageForm, self).__init__(*args, **kwargs)
        simple_form_widget(
            self=self, field='name', maxlength=50, pattern="^[_A-z0-9 .,'-#]{1,}$",
            placeholder='Enter equipment name...'
        )
        simple_form_widget(
            self=self, field='length', step=00.01, pattern="^[0-9.]{1,}$", placeholder='Enter length (in feet)...'
        )
        simple_form_widget(
            self=self, field='height', step=00.01, pattern="^[0-9.]{1,}$", placeholder='Enter height (in feet)...'
        )
        simple_form_widget(
            self=self, field='width', step=00.01, pattern="^[0-9.]{1,}$", placeholder='Enter width (in feet)...'
        )

    class Meta:
        model = Cage
        fields = [
            'name', 'length', 'height', 'width', 'cover_type'
        ]


class MaintenanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'id': 'datepicker1',
            'autocomplete': 'off'
        })
        self.fields['start_time'].widget.attrs.update({
            'id': 'hiddendatepicker1',
            'autocomplete': 'off'
        })
        self.fields['end_time'].widget.attrs.update({
            'id': 'hiddendatepicker2',
            'autocomplete': 'off'
        })
        self.fields['staff'].help_text = "Hold down “Control”, or “Command” on a Mac, to select more than one."
        self.fields['equipment_set'].help_text = "Hold down “Control”, or “Command” on a Mac, to select more than one."
    class Meta:
        model = Maintenance
        fields = [
            'cage', 'staff', 'date', 'start_time', 'end_time', 'equipment_set'
        ]


    def clean_end_time(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if not end_time == None:
            # today = datetime.datetime.now()
            if not end_time > start_time:
                raise forms.ValidationError(
                    'End time must be greater than start time!')
            return end_time
        return None
