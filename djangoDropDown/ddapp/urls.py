from  django.urls import path
from .views import HomePageView, load_cities


urlpatterns=[
     path('',HomePageView,name='home'),
     path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
     path('ajax/load-city_dd/', load_cities, name='ajax_load_city_dd')
     
]