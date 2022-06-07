from django import forms
from django.shortcuts import render

from django import forms
from ..home_page.models import Planet


class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = "__all__"