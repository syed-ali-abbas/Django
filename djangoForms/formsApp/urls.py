from django.urls import path
from .views import HomePageView, BlogCreateView, BlogDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')

]