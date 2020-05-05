from django.shortcuts import render
from staff.models import Staff
from animal.models import Animal, AnimalCage, Cage, HealthPoint, Species
from food.models import Food, AnimalFood
from health.models import AnimalTreatment, Disease, Medicine
from maintenance.models import Cage, Incident, Equipment, EquipmentSet, Maintenance
from django.views.generic import TemplateView
import datetime
from util.helpers import get_report
from util.view_imports import *


@method_decorator(login_required, name='dispatch')
@method_decorator(high_level_staff_required, name='dispatch')
class ReportTemplateView(TemplateView):
    template_name = "snippets/reports/reports.html"

    def get_context_data(self, **kwargs):
        context = super(ReportTemplateView, self).get_context_data(**kwargs)
        context['page_title'] = "Reports"
        # Report Data Starts
        query_context = self.request.GET.get('q')
        query_context_date_from = self.request.GET.get('date-from')
        query_context_date_to = self.request.GET.get('date-to')
        query_in = self.request.GET.get('query-in')
        context['query'] = query_context
        context['query_date_from'] = query_context_date_from
        context['query_date_to'] = query_context_date_to
        context['query_in'] = query_in
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        date_from_filtered = method_dict.get('date-from', None)
        date_to_filtered = method_dict.get('date-to', None)
        query_in_filtered = method_dict.get('query-in', None)
        
        # Acquiring User Defined Model
        if query_in_filtered == "Animal":
            selected_model = Animal
        elif query_in_filtered == "AnimalCage":
            selected_model = AnimalCage
        elif query_in_filtered == "Food":
            selected_model = Food
        elif query_in_filtered == "AnimalFood":
            selected_model = AnimalFood
        elif query_in_filtered == "Disease":
            selected_model = Disease
        elif query_in_filtered == "AnimalTreatment":
            selected_model = AnimalTreatment
        elif query_in_filtered == "Cage":
            selected_model = Cage
        elif query_in_filtered == "Maintenance":
            selected_model = Maintenance
        elif query_in_filtered == "Incident":
            selected_model = Incident
        elif query_in_filtered == "Staff":
            selected_model = Staff
        else:
            selected_model = Animal
            query_in_filtered = "Animal"

        # Getting the Actual Report
        get_report(
            context=context, context_name=str(query_in_filtered).lower(), model=selected_model, query=query,
            date_from_filtered=date_from_filtered, date_to_filtered=date_to_filtered
        )

        return context

