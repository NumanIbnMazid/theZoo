from django.shortcuts import render
from .forms import (
    SpeciesForm, HealthPointForm, AnimalForm, AnimalCageForm
)
from .models import (
    Species, HealthPoint, Animal, AnimalCage
)
from django import forms
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Q
import datetime
from util.helpers import (
    validate_normal_form, simple_context_data, get_simple_object, delete_simple_object
)
from staff.models import Staff
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Custom Decorators Starts
from accounts.decorators import (
    is_superuser_required, high_level_staff_required, mid_level_staff_required, low_level_staff_required
)
# decorators = [
#     login_required, is_superuser_required
# ]


# ------------------- Species -------------------

@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class SpeciesCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = SpeciesForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Species.objects.filter(
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
        return reverse('animal:add_species')

    def get_context_data(self, **kwargs):
        context = super(
            SpeciesCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Species,
            page_title='Create Species',
            update_url='animal:update_species',
            delete_url='animal:delete_species',
            namespace='species'
        )

    def user_passes_test(self, request):
        user = request.user
        staff = Staff.objects.filter(user=user).first()
        if staff.role in ["Mid Level", "High Level"] or staff.user.is_superuser:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        instance_user = self.request.user
        if not self.user_passes_test(request):
            messages.add_message(self.request, messages.ERROR,
                                    "You are not allowed !"
                                )
            return HttpResponseRedirect(reverse('home'))
        return super(SpeciesCreateView, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class SpeciesUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = SpeciesForm

    def get_object(self):
        return get_simple_object(key='id', model=Species, self=self)

    def form_valid(self, form):
        name = form.instance.name
        obj_id = self.get_object().id
        field_qs = Species.objects.filter(
            name__iexact=name
        ).exclude(id=obj_id)
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('animal:add_species')

    def get_context_data(self, **kwargs):
        context = super(
            SpeciesUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Species,
            page_title='Update Species',
            update_url='animal:update_species',
            delete_url='animal:delete_species',
            namespace='species'
        )


@csrf_exempt
def delete_species(request):
    return delete_simple_object(request=request, key='id', model=Species)


# ------------------- HealthPoint -------------------

@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class HealthPointCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = HealthPointForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = HealthPoint.objects.filter(
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
        return reverse('animal:add_health_point')

    def get_context_data(self, **kwargs):
        context = super(
            HealthPointCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=HealthPoint,
            page_title='Create Health Point',
            update_url='animal:update_health_point',
            delete_url='animal:delete_health_point',
            namespace='health_point'
        )


@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class HealthPointUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = HealthPointForm

    def get_object(self):
        return get_simple_object(key='id', model=HealthPoint, self=self)

    def form_valid(self, form):
        name = form.instance.name
        obj_id = self.get_object().id
        field_qs = HealthPoint.objects.filter(
            name__iexact=name
        ).exclude(id=obj_id)
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('animal:add_health_point')

    def get_context_data(self, **kwargs):
        context = super(
            HealthPointUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=HealthPoint,
            page_title='Update Health Point',
            update_url='animal:update_health_point',
            delete_url='animal:delete_health_point',
            namespace='health_point'
        )


@csrf_exempt
def delete_health_point(request):
    return delete_simple_object(request=request, key='id', model=HealthPoint)


# ------------------- Animal -------------------

@method_decorator(login_required, name='dispatch')
@method_decorator(mid_level_staff_required, name='dispatch')
class AnimalCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalForm

    def form_valid(self, form):
        name = form.instance.name
        slug = form.instance.slug
        field_qs = Animal.objects.filter(
            name__iexact=name, slug=slug
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
        return reverse('animal:add_animal')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Animal,
            page_title='Create Animal',
            update_url='animal:update_animal',
            delete_url='animal:delete_animal',
            namespace='animal'
        )


@method_decorator(login_required, name='dispatch')
@method_decorator(mid_level_staff_required, name='dispatch')
class AnimalUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalForm

    def get_object(self):
        return get_simple_object(key='id', model=Animal, self=self)

    def form_valid(self, form):
        name = form.instance.name
        predata = self.get_object().name
        field_qs = Animal.objects.filter(
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
        return reverse('animal:add_animal')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Animal,
            page_title='Update Animal',
            update_url='animal:update_animal',
            delete_url='animal:delete_animal',
            namespace='animal'
        )


@csrf_exempt
def delete_animal(request):
    return delete_simple_object(request=request, key='id', model=Animal)


# ------------------- AnimalCage -------------------

@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class AnimalCageCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalCageForm

    def form_valid(self, form):
        animal = form.instance.animal
        field_qs = AnimalCage.objects.filter(
            animal=animal
        )
        result = validate_normal_form(
            field='animal', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('animal:add_animal_cage')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalCageCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=AnimalCage,
            page_title='Assign Animal to Cage',
            update_url='animal:update_animal_cage',
            delete_url='animal:delete_animal_cage',
            namespace='animal_cage'
        )


@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class AnimalCageUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalCageForm

    def get_object(self):
        return get_simple_object(key='id', model=AnimalCage, self=self)

    def form_valid(self, form):
        animal = form.instance.animal
        field_qs = AnimalCage.objects.filter(
            animal=animal
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='animal', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('animal:add_animal_cage')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalCageUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=AnimalCage,
            page_title='Update Animal Cage',
            update_url='animal:update_animal_cage',
            delete_url='animal:delete_animal_cage',
            namespace='animal_cage'
        )


@csrf_exempt
def delete_animal_cage(request):
    return delete_simple_object(request=request, key='id', model=AnimalCage)
