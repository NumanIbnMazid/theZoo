from util.helpers import (
    validate_normal_form, simple_context_data, get_simple_object, delete_simple_object
)
from django.shortcuts import render
from .forms import (
    UserStaffForm, BaseUserForm, AdminUserStaffForm
)
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse
from .models import Staff
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Custom Decorators Starts
from accounts.decorators import (
    is_superuser_required
)
decorators = [login_required, is_superuser_required]


@method_decorator(decorators, name='dispatch')
class StaffCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = BaseUserForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        email_qs = User.objects.filter(
            email__iexact=email
        )
        if email_qs.exists():
            form.add_error(
                'email', forms.ValidationError(
                    "This email is already registered ! Please try another one."
                )
            )
            return super().form_invalid(form)
        # user = form.save(commit=False)
        # user.set_password(form.cleaned_data["password"])
        messages.add_message(
            self.request, messages.SUCCESS,
            "Staff created successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('staff:list_staff')

    def get_context_data(self, **kwargs):
        context = super(
            StaffCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Add Staff'
        context['delete_url'] = 'staff:delete_staff'
        return context


@method_decorator(login_required, name='dispatch')
class StaffUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = UserStaffForm

    def get_object(self):
        id = self.kwargs['id']
        qs = Staff.objects.filter(
            id=id
        )
        if qs.exists():
            return qs.first()
        return None

    def form_valid(self, form):
        email = form.instance.email
        username = form.instance.username
        field_qs = Staff.objects.filter(
            email__iexact=email
        ).exclude(id=self.get_object().id)
        field_qs_username = Staff.objects.filter(
            username__iexact=username
        ).exclude(id=self.get_object().id)
        if field_qs.exists():
            form.add_error(
                'email', forms.ValidationError(
                    "This email is already exists! Please try another one."
                )
            )
            return super().form_invalid(form)
        if field_qs_username.exists():
            form.add_error(
                'username', forms.ValidationError(
                    "This username is already exists! Please try another one."
                )
            )
            return super().form_invalid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            "Updated successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('staff:list_staff')

    def get_context_data(self, **kwargs):
        context = super(
            StaffUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Update Staff'
        return context


@method_decorator(decorators, name='dispatch')
class AdminStaffUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = AdminUserStaffForm

    def get_object(self):
        id = self.kwargs['id']
        qs = Staff.objects.filter(
            id=id
        )
        if qs.exists():
            return qs.first()
        return None

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS,
            "Updated successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('staff:list_staff')

    def get_context_data(self, **kwargs):
        context = super(
            AdminStaffUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Update Staff'
        return context


class StaffListView(ListView):
    template_name = 'staff/list.html'

    def get_queryset(self):
        query = Staff.objects.all()
        return query

    def get_context_data(self, **kwargs):
        context = super(
            StaffListView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Staff List'
        context['delete_url'] = 'staff:delete_staff'
        context['namespace'] = 'staff'
        return context

    
@method_decorator(login_required, name='dispatch')
class StaffDetailView(DetailView):
    template_name = 'staff/details.html'

    def get_object(self):
        qs = Staff.objects.filter(id=self.kwargs['id'])
        if qs.exists():
            return qs.first()
        return None


@csrf_exempt
def delete_staff(request):
    return delete_simple_object(request=request, key='id', model=Staff)
