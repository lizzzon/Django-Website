from django.urls import path, include
from apps.authentication.views import RegisterFormView, LoginFormView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginFormView.as_view(), name="login"),
    path('register/', RegisterFormView.as_view(), name='register'),
]