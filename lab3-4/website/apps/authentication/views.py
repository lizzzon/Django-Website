from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/auth/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "registration/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user())
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")