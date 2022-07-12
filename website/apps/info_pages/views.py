from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.home_page.models import Planet
from multiprocessing import Pool


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


p = Pool(3)
def f(x): return x
threads = [p.apply_async(f, [i]) for i in range(20)]
for t in threads:
    try: print(t.get(timeout=1))
    except Exception: pass
