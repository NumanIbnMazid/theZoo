from django.contrib import admin
from util.mixins import CustomModelAdminMixin
from .models import Staff
from django.contrib.auth.admin import UserAdmin


UserAdmin.list_display += ('is_active',)

class StaffAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Staff


admin.site.register(Staff, StaffAdmin)
