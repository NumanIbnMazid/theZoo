from django import template
from django.contrib import messages
from django.contrib.auth.models import User
from staff.models import Staff
from django.db.models import Q

register = template.Library()


@register.simple_tag(takes_context=True)
def get_superuser(context):
    request = context['request']
    super_user_qs = User.objects.filter(is_superuser=True)
    if super_user_qs.exists() and request.user.is_superuser:
        return True
    return False


@register.simple_tag(takes_context=True)
def get_high_level_staff(context):
    request = context['request']
    high_level_staff_qs = Staff.objects.filter(role__iexact="High Level", user=request.user)
    if high_level_staff_qs.exists() or request.user.is_superuser:
        return True
    return False


@register.simple_tag(takes_context=True)
def get_mid_level_staff(context):
    request = context['request']
    mid_level_staff_qs = Staff.objects.filter(
        Q(role__iexact="High Level") | Q(role__iexact="Mid Level"),
        user=request.user
    )
    if mid_level_staff_qs.exists() or request.user.is_superuser:
        return True
    return False


@register.simple_tag(takes_context=True)
def get_low_level_staff(context):
    request = context['request']
    low_level_staff_qs = Staff.objects.filter(
        Q(role__iexact="High Level") | 
        Q(role__iexact="Mid Level") | 
        Q(role__iexact="Low Level"),
        user=request.user
    )
    if low_level_staff_qs.exists() or request.user.is_superuser:
        return True
    return False
