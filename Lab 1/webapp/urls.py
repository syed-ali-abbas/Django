from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView, AboutPageView, BlogDetailView 

urlpatterns =[
     path('',HomePageView.as_view(),name='home'),
     path('blogs', BlogPageView.as_view(), name='blogs'),
     path('about', AboutPageView.as_view(),name='about'),
     path('contact',ContactPageView.as_view(),name='contact'),
     path('blogs/<int:pk>/', BlogDetailView.as_view(), name='detailed_posts')
]