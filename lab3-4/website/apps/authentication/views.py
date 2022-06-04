from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.authentication.forms import RegisterForm, LoginForm


class MyView(LoginRequiredMixin, View):
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'


class RegisterFormView(View):
    form_class = UserCreationForm

    success_url = "/auth/login/"
    template_name = "registration/register.html"

    def get(self, request):
        form = RegisterForm()
        return render(request, "registration/register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, email=email, password1=raw_password, password2=password)

        return render(request, "registration/register.html", {'form': form})


class LoginFormView(View):
    form_class = AuthenticationForm
    template_name = "registration/login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "registration/login.html", {'form': form})

    def login(self, request):
        form = LoginForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = AuthenticationForm()
        return render(request, "registration/login.html", {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
