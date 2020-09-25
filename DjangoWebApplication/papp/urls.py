from .views import HomepageView, UpdateHomepage, CreatePostView, PostDetailView,PostDelete
from django.urls import path

urlpatterns = [
    path('', HomepageView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', CreatePostView.as_view(), name = 'post'),
    path('post/<int:pk>/edit/', UpdateHomepage.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/',PostDelete.as_view(), name = 'post_delete' )
]