# coding: utf-8

from django.urls import re_path as url, include
from rest_framework.routers import SimpleRouter

from .views import ParkViewSet, ParkDataViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'parks', ParkViewSet)
router.register(r'parkdata', ParkDataViewSet)


##### Aggiunta degli url ####################################
app_name = 'park'
urlpatterns =  [
    url(r'^', include(router.urls)),    
]
