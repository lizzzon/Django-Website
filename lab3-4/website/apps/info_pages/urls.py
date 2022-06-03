from django.urls import path

from .views import *

urlpatterns = [
    path('planets/<str:planet_name>/', planets),
]