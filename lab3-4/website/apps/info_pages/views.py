from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.home_page.models import Planet


class InfoPage(ListView):
    model = Planet
    template_name = 'main/about.html'
    context_object_name = 'info'


class PlanetList(ListView):
    model = Planet
    context_object_name = 'planets'
    template_name = 'main/blog.html'


class PlanetDetail(DetailView):
    model = Planet
    context_object_name = 'planet'
    template_name = 'main/blog.html'


class PlanetCreate(CreateView):
    model = Planet
    fields = '__all__'
    template_name = 'main/create.html'
    success_url = reverse_lazy('blog')


class PlanetUpdate(UpdateView):
    model = Planet
    fields = '__all__'
    template_name = 'main/create.html'
    success_url = reverse_lazy('blog')


class DeleteView(DeleteView):
    model = Planet
    context_object_name = 'planet'
    success_url = reverse_lazy('blog')



