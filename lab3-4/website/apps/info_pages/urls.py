from django.urls import path
from apps.info_pages.views import InfoPage, PlanetCreate, PlanetDetail, PlanetUpdate, PlanetList, PlanetDelete

urlpatterns = [
    path('', InfoPage.as_view(), name='info'),
    path('blog/', PlanetList.as_view(), name='blog'),
    path('planet/<int:pk>', PlanetDetail.as_view(), name='planet'),
    path('create-planet/', PlanetCreate.as_view(), name='create-planet'),
    path('update-planet/', PlanetUpdate.as_view(), name='update-planet'),
    path('delete-planet/', PlanetDelete.as_view(), name='delete-planet'),
]
