from django.urls import path, include
from apps.authentication.views import RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('sign_out/', LogoutView.as_view(next_page='home'), name="sign_out"),
    path('registration/', RegisterPage.as_view(), name='registration'),
]