from django.urls import path, include
from .views import (
    StaffCreateView, StaffUpdateView, StaffListView, delete_staff, AdminStaffUpdateView,
    StaffDetailView
)


urlpatterns = [
    path('<id>/view/',
         StaffDetailView.as_view(), name='staff_details'),
    path('<id>/update/',
         StaffUpdateView.as_view(), name='update_staff'),
    path('list/',
         StaffListView.as_view(), name='list_staff'),
    path('add/staff/',
         StaffCreateView.as_view(), name='add_staff'),
    path('delete/', delete_staff, name='delete_staff'),
    path('<id>/admin/update/',
         AdminStaffUpdateView.as_view(), name='update_staff_admin'),
]
