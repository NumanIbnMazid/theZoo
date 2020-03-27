from django.shortcuts import render
from util.view_imports import *
from .models import (
    Medicine, Disease, AnimalTreatment
)
from .forms import (
    MedicineForm, DiseaseForm, AnimalTreatmentForm
)


# ------------------- Medicine -------------------

@method_decorator(login_required, name='dispatch')
class MedicineCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = MedicineForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Medicine.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('health:add_medicine')

    def get_context_data(self, **kwargs):
        context = super(
            MedicineCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Medicine,
            page_title='Create Medicine',
            update_url='health:update_medicine',
            delete_url='health:delete_medicine',
            namespace='medicine'
        )


@method_decorator(login_required, name='dispatch')
class MedicineUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = MedicineForm

    def get_object(self):
        return get_simple_object(key='id', model=Medicine, self=self)

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Medicine.objects.filter(
            name__iexact=name
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('health:add_medicine')

    def get_context_data(self, **kwargs):
        context = super(
            MedicineUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Medicine,
            page_title='Update Medicine',
            update_url='health:update_medicine',
            delete_url='health:delete_medicine',
            namespace='medicine'
        )


@csrf_exempt
def delete_medicine(request):
    return delete_simple_object(request=request, key='id', model=Medicine)


# ------------------- Disease -------------------


@method_decorator(login_required, name='dispatch')
class DiseaseCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = DiseaseForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Disease.objects.filter(
            name__iexact=name, animal=form.instance.animal, date__iexact=form.instance.date
        )
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('health:add_disease')

    def get_context_data(self, **kwargs):
        context = super(
            DiseaseCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Disease,
            page_title='Create Disease',
            update_url='health:update_disease',
            delete_url='health:delete_disease',
            namespace='disease'
        )


@method_decorator(login_required, name='dispatch')
class DiseaseUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = DiseaseForm

    def get_object(self):
        return get_simple_object(key='id', model=Disease, self=self)

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Disease.objects.filter(
            name__iexact=name, animal=form.instance.animal, date__iexact=form.instance.date
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('health:add_disease')

    def get_context_data(self, **kwargs):
        context = super(
            DiseaseUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Disease,
            page_title='Update Disease',
            update_url='health:update_disease',
            delete_url='health:delete_disease',
            namespace='disease'
        )


@csrf_exempt
def delete_disease(request):
    return delete_simple_object(request=request, key='id', model=Disease)


# ------------------- AnimalTreatment -------------------


@method_decorator(login_required, name='dispatch')
class AnimalTreatmentCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalTreatmentForm

    def form_valid(self, form):
        field_qs = None
        result = validate_normal_form(
            field=None, field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('health:add_animal_treatment')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalTreatmentCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=AnimalTreatment,
            page_title='Create AnimalTreatment',
            update_url='health:update_animal_treatment',
            delete_url='health:delete_animal_treatment',
            namespace='animal_treatment'
        )


@method_decorator(login_required, name='dispatch')
class AnimalTreatmentUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalTreatmentForm

    def get_object(self):
        return get_simple_object(key='id', model=AnimalTreatment, self=self)

    def form_valid(self, form):
        field_qs = None
        result = validate_normal_form(
            field=None, field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('health:add_animal_treatment')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalTreatmentUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=AnimalTreatment,
            page_title='Update AnimalTreatment',
            update_url='health:update_animal_treatment',
            delete_url='health:delete_animal_treatment',
            namespace='animal_treatment'
        )


@csrf_exempt
def delete_animal_treatment(request):
    return delete_simple_object(request=request, key='id', model=AnimalTreatment)
