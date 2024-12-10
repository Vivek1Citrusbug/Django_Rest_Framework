from .views import BlogCreateView,BlogDetailView,BlogPostDeleteView,BlogPostListingView,BlogUpdateView
from django.urls import path,include


urlpatterns = [
    path('', BlogPostListingView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
    # path('<int:pk>/comments/',include('comments.urls')),
    path('new/', BlogCreateView.as_view(), name='blog_create'),
]