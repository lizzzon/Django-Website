from django.views.generic import ListView
from apps.home_page.models import Planet


class HomePage(ListView):
    model = Planet
    template_name = 'main/base.html'
    context_object_name = 'info'

