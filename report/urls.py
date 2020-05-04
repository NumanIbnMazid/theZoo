from django.urls import path, include
from .views import ReportTemplateView


urlpatterns = [
    path("view/", ReportTemplateView.as_view(), name="report_view")
]
