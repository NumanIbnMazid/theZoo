from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponseRedirect
from django.db.models import Q
import datetime
from .models import (
    Equipment, EquipmentSet, Cage, Maintenance, Incident
)
from util.helpers import (
    validate_normal_form, simple_context_data, get_simple_object, delete_simple_object
)
from .forms import (
    EquipmentForm, EquipmentSetForm, CageForm, MaintenanceForm, IncidentForm
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Custom Decorators Starts
from accounts.decorators import (
    is_superuser_required
)
decorators = [login_required, is_superuser_required]


# ------------------- Equipment -------------------

@method_decorator(login_required, name='dispatch')
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
            model=Equipment, form=form, request=self.request
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


@method_decorator(login_required, name='dispatch')
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
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=Equipment, form=form, request=self.request
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

@method_decorator(login_required, name='dispatch')
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
            model=EquipmentSet, form=form, request=self.request
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


@method_decorator(login_required, name='dispatch')
class EquipmentSetUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = EquipmentSetForm

    def get_object(self):
        return get_simple_object(key='id', model=EquipmentSet, self=self)

    def form_valid(self, form):
        name = form.instance.name
        predata = self.get_object().name
        field_qs = EquipmentSet.objects.filter(
            name__iexact=name
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=EquipmentSet, form=form, request=self.request
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


# ------------------- Cage -------------------

@method_decorator(login_required, name='dispatch')
class CageCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = CageForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Cage.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=Cage, form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_cage')

    def get_context_data(self, **kwargs):
        context = super(
            CageCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Cage,
            page_title='Create Cage',
            update_url='maintenance:update_cage',
            delete_url='maintenance:delete_cage',
            namespace='cage'
        )


@method_decorator(login_required, name='dispatch')
class CageUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = CageForm

    def get_object(self):
        return get_simple_object(key='id', model=Cage, self=self)

    def form_valid(self, form):
        name = form.instance.name
        predata = self.get_object().name
        field_qs = Cage.objects.filter(
            name__iexact=name
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='name', field_data=name, field_qs=field_qs,
            model=Cage, form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_cage')

    def get_context_data(self, **kwargs):
        context = super(
            CageUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Cage,
            page_title='Update Cage',
            update_url='maintenance:update_cage',
            delete_url='maintenance:delete_cage',
            namespace='cage'
        )


@csrf_exempt
def delete_cage(request):
    return delete_simple_object(request=request, key='id', model=Cage)


# ------------------- Maintenance -------------------

@method_decorator(login_required, name='dispatch')
class MaintenanceCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = MaintenanceForm

    # def post(self, request, *args, **kwargs):
    #     response = super(MaintenanceCreateView, self).post(
    #         request, *args, **kwargs)
    #     form = self.get_form_class()
    #     data = request.POST.copy()
    #     # date = data.get('date')
    #     # start_time = data.get('start_time')
    #     # str_date = str(date).split('-')
    #     # str_start_time = str(start_time).split(':')
    #     # start_date = datetime.datetime(
    #     #     int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
    #     #         str_start_time[0]), int(str_start_time[1])
    #     # )
    #     # form.start_time = datetime.datetime.now()
    #     # form.cleaned_data['start_time'] = datetime.datetime.now()
    #     # form.save(self)
    #     # print('BBBB', form.start_time)
    #     return response

    def form_valid(self, form):
        cage = form.instance.cage
        date = form.instance.date
        start_t = form.instance.start_time
        end_t = form.instance.end_time
        # Date Binding
        str_date = str(date).split('-')
        str_start_time = str(start_t).split(" ")[1].split(":")[0]
        str_end_time = str(end_t).split(" ")[1].split(":")[0]
        start_time = datetime.datetime(
            int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
                str_start_time), 00
        )
        end_time = datetime.datetime(
            int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
                str_end_time), 00
        )
        # Saving Object
        form.instance.start_time = start_time
        form.instance.end_time = end_time
        # print("xxxx", str(start_time))
        query_set = Maintenance.objects.filter(
            cage__name__iexact=cage,
        ).filter(
            Q(start_time__gt=start_time, end_time__lt=end_time) |
            Q(end_time__gt=start_time, start_time__lt=end_time)
        )
        # .filter(
        #     Q(start_time__range=[str(start_time), str(end_time)]) |
        #     Q(end_time__range=[str(start_time), str(end_time)])
        # )
        if query_set.exists():
            form.add_error(
                None, forms.ValidationError(
                    "There's already remain a schedule between date time range for that Cage!")
            )
            messages.add_message(
                self.request, messages.WARNING,
                "Not Saved!"
            )
            return super().form_invalid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            "Created successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('maintenance:add_maintenance')

    def get_context_data(self, **kwargs):
        context = super(
            MaintenanceCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Maintenance,
            page_title='Create Maintenance',
            update_url='maintenance:update_maintenance',
            delete_url='maintenance:delete_maintenance',
            namespace='maintenance'
        )


@method_decorator(login_required, name='dispatch')
class MaintenanceUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = MaintenanceForm

    def get_object(self):
        return get_simple_object(key='id', model=Maintenance, self=self)

    def form_valid(self, form):
        cage = form.instance.cage
        date = form.instance.date
        start_t = form.instance.start_time
        end_t = form.instance.end_time
        # Date Binding
        str_date = str(date).split('-')
        str_start_time = str(start_t).split(" ")[1].split(":")[0]
        str_end_time = str(end_t).split(" ")[1].split(":")[0]
        start_time = datetime.datetime(
            int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
                str_start_time), 00
        )
        end_time = datetime.datetime(
            int(str_date[0]), int(str_date[1]), int(str_date[2]), int(
                str_end_time), 00
        )
        # Saving Object
        form.instance.start_time = start_time
        form.instance.end_time = end_time
        # print("xxxx", str(start_time))
        query_set = Maintenance.objects.filter(
            cage__name__iexact=cage,
        ).filter(
            Q(start_time__gt=start_time, end_time__lt=end_time) |
            Q(end_time__gt=start_time, start_time__lt=end_time)
        ).exclude(id=self.get_object().id)
        # .filter(
        #     Q(start_time__range=[str(start_time), str(end_time)]) |
        #     Q(end_time__range=[str(start_time), str(end_time)])
        # )
        if query_set.exists():
            form.add_error(
                None, forms.ValidationError(
                    "There's already remain a schedule between date time range for that Cage!")
            )
            messages.add_message(
                self.request, messages.WARNING,
                "Not Saved!"
            )
            return super().form_invalid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            "Updated successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('maintenance:add_maintenance')

    def get_context_data(self, **kwargs):
        context = super(
            MaintenanceUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Maintenance,
            page_title='Update Maintenance',
            update_url='maintenance:update_maintenance',
            delete_url='maintenance:delete_maintenance',
            namespace='maintenance'
        )


@csrf_exempt
def delete_maintenance(request):
    return delete_simple_object(request=request, key='id', model=Maintenance)


# ------------------- Incident -------------------

@method_decorator(login_required, name='dispatch')
class IncidentCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = IncidentForm

    def form_valid(self, form):
        title = form.instance.title
        field_qs = Incident.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='title', field_data=title, field_qs=field_qs,
            model=Incident, form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_incident')

    def get_context_data(self, **kwargs):
        context = super(
            IncidentCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Incident,
            page_title='Create Incident',
            update_url='maintenance:update_incident',
            delete_url='maintenance:delete_incident',
            namespace='incident'
        )


@method_decorator(login_required, name='dispatch')
class IncidentUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = IncidentForm

    def get_object(self):
        return get_simple_object(key='id', model=Incident, self=self)

    def form_valid(self, form):
        title = form.instance.title
        predata = self.get_object().title
        field_qs = Incident.objects.filter(
            title__iexact=title
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='title', field_data=title, field_qs=field_qs,
            model=Incident, form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('maintenance:add_incident')

    def get_context_data(self, **kwargs):
        context = super(
            IncidentUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Incident,
            page_title='Update Incident',
            update_url='maintenance:update_incident',
            delete_url='maintenance:delete_incident',
            namespace='incident'
        )


@csrf_exempt
def delete_incident(request):
    return delete_simple_object(request=request, key='id', model=Incident)
