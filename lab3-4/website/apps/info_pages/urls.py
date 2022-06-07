from django.urls import path
from apps.info_pages.views import *

urlpatterns = [
    path('', InfoPage.as_view(), name='info'),
    path('/blog', PlanetList.as_view(), name='blog'),
    path('planet/<int:pk>/', PlanetDetail.as_view(), name='planet'),
    path('create-planet/', PlanetCreate.as_view(), name='create'),
    path('update-planet/<int:pk>/', PlanetUpdate.as_view(), name='update'),
    path('delete-planet/<int:pk>/', DeleteView.as_view(), name='delete'),
]