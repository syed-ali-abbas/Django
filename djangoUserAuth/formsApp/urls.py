from django.urls import path
from .views import HomePageView, BlogCreateView, BlogDetailView, BlogUpdate, BlogDeletion


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',BlogUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeletion.as_view(), name='post_delete')

]