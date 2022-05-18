from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("apps.authentication.urls")),
]
