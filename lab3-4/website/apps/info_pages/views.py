from django.http import HttpResponse
from django.views.generic import ListView
from apps.home_page.models import Planet


def planets(request, planet_name):
    return HttpResponse(f"<h1>Planets</h1><p>{planet_name}</p>")

