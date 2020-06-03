from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import statistics101.urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(statistics101.urls, namespace='statistics101')),
    path('accounts/', include('django.contrib.auth.urls')),
]
