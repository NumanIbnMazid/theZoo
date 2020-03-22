from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponseRedirect
from .models import (
    Equipment, EquipmentSet, Cage, Maintenance, Incident
)
from util.helpers import (
    validate_normal_form, simple_context_data, get_simple_object, delete_simple_object
)
from .forms import (
    EquipmentForm, EquipmentSetForm
)


# ------------------- Equipment -------------------

class EquipmentCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = EquipmentForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Equipment.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=Equipment, form=form, request=self.request, view_type='create'
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_equipment')

    def get_context_data(self, **kwargs):
        context = super(
            EquipmentCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Equipment,
            page_title='Create Equipment',
            update_url='maintenance:update_equipment',
            delete_url='maintenance:delete_equipment',
            namespace='equipment'
        )


class EquipmentUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = EquipmentForm

    def get_object(self):
        return get_simple_object(key='id', model=Equipment, self=self)

    def form_valid(self, form):
        name = form.instance.name
        predata = self.get_object().name
        field_qs = Equipment.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=Equipment, form=form, request=self.request, view_type='update',
            predata=predata
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_equipment')

    def get_context_data(self, **kwargs):
        context = super(
            EquipmentUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Equipment,
            page_title='Update Equipment',
            update_url='maintenance:update_equipment',
            delete_url='maintenance:delete_equipment',
            namespace='equipment'
        )


@csrf_exempt
def delete_equipment(request):
    return delete_simple_object(request=request, key='id', model=Equipment)


# ------------------- Equipment Set -------------------

class EquipmentSetCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = EquipmentSetForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = EquipmentSet.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=EquipmentSet, form=form, request=self.request, view_type='create'
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_equipment_set')

    def get_context_data(self, **kwargs):
        context = super(
            EquipmentSetCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=EquipmentSet,
            page_title='Create Equipment Set',
            update_url='maintenance:update_equipment_set',
            delete_url='maintenance:delete_equipment_set',
            namespace='equipment_set'
        )


class EquipmentSetUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = EquipmentSetForm

    def get_object(self):
        return get_simple_object(key='id', model=EquipmentSet, self=self)

    def form_valid(self, form):
        name = form.instance.name
        predata = self.get_object().name
        print(name, predata)
        field_qs = EquipmentSet.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=EquipmentSet, form=form, request=self.request, view_type='update',
            predata=predata
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
        # return super().form_valid(form)

    def get_success_url(self):
        return reverse('maintenance:add_equipment_set')

    def get_context_data(self, **kwargs):
        context = super(
            EquipmentSetUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=EquipmentSet,
            page_title='Update Equipment Set',
            update_url='maintenance:update_equipment_set',
            delete_url='maintenance:delete_equipment_set',
            namespace='equipment_set'
        )


@csrf_exempt
def delete_equipment_set(request):
    return delete_simple_object(request=request, key='id', model=EquipmentSet)
