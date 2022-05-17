from django.urls import path, include
from website.apps.authentication.views import RegisterFormView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', RegisterFormView.as_view(), name='register'),
]