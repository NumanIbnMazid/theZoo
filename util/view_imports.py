from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponseRedirect
from django.db.models import Q
import datetime
from util.helpers import (
    validate_normal_form, simple_context_data, get_simple_object, delete_simple_object
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Custom Decorators Starts
from accounts.decorators import (
    is_superuser_required
)
decorators = [login_required, is_superuser_required]
