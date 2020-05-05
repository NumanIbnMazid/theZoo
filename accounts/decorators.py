from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings


# Super Admin Required

is_superuser_required = user_passes_test(
    lambda user: user.is_superuser == True, login_url=settings.HOME_URL)


def can_browse_required(view_func):
    decorated_view_func = login_required(is_superuser_required(view_func))
    return decorated_view_func


# High Level Staff Required
staff_is_high_level = user_passes_test(
    lambda user: user.user_staff.role in ["High Level"] or user.is_superuser, login_url=settings.HOME_URL)


def high_level_staff_required(view_func):
    decorated_view_func = login_required(staff_is_high_level(view_func))
    return decorated_view_func

# Mid Level Staff Required
staff_is_mid_level = user_passes_test(
    lambda user: user.user_staff.role in ["High Level", "Mid Level"] or user.is_superuser, login_url=settings.HOME_URL)


def mid_level_staff_required(view_func):
    decorated_view_func = login_required(staff_is_mid_level(view_func))
    return decorated_view_func

# Low Level Staff Required
staff_is_low_level = user_passes_test(
    lambda user: user.user_staff.role in ["High Level", "Mid Level", "Low Level"] or user.is_superuser, login_url=settings.HOME_URL)


def low_level_staff_required(view_func):
    decorated_view_func = login_required(staff_is_low_level(view_func))
    return decorated_view_func
