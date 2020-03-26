from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('account/', include('accounts.urls')),
    path('staff/', include(('staff.urls', 'staff'), namespace='staff')),
    path('maintenance/', include(('maintenance.urls', 'maintenance'), namespace='maintenance')),
    path('animal/', include(('animal.urls', 'animal'), namespace='animal')),
    path('food/', include(('food.urls', 'food'), namespace='food')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
