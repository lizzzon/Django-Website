from django.views.generic import ListView, CreateView, DetailView
from django.urls import  reverse_lazy
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView

from apps.home_page.forms import PlanetForm
from apps.home_page.models import Planet


class InfoPage(ListView):
    model = Planet
    template_name = 'main/about.html'
    context_object_name = 'info'


class PlanetList(ListView):
    model = Planet
    context_object_name = 'planets'


class PlanetDetail(DetailView):
    model = Planet
    context_object_name = 'planet'
    template_name = 'main/blog.html'


class PlanetCreate(CreateView):
    model = Planet
    fields = '__all__'
    success_url = reverse_lazy('blog')


class PlanetUpdate(UpdateView):
    model = Planet
    fields = '__all__'
    success_url = reverse_lazy('blog')


class PlanetDelete(DeleteView):
    model = Planet
    context_object_name = 'planets'
    success_url = reverse_lazy('blog')

