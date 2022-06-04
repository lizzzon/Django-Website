from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'from-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'from-input'}))

    class Temp:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'from-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'from-input'}))