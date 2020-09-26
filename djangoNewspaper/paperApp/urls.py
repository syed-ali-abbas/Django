from django.urls import path
from .views import HomePageView,signupPageView

urlpatterns =  [
    path('signup/', signupPageView.as_view(), name='signup'),
    path('',HomePageView.as_view(), name = 'home')
]