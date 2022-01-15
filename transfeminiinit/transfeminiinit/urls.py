from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='website/', permanent=True)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
