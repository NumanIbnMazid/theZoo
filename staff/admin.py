from django.contrib import admin
from util.mixins import CustomModelAdminMixin
from .models import Staff

class StaffAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Staff


admin.site.register(Staff, StaffAdmin)
