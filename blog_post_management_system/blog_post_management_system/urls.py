"""
URL configuration for blog_post_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import home_page

from rest_framework.routers import DefaultRouter
from blogs.views import BlogPostListingAPIView,CommentListView

router = DefaultRouter()
router.register(r'Blogs',BlogPostListingAPIView,basename='blogpost')


urlpatterns = [
    path("",views.home_page,name = 'home_page'),
    path('admin/', admin.site.urls, name = "admin_view"),
    path("accounts/",include("accounts.urls")),
    path("api/",include(router.urls)),
    path("api/Blogs/<int:blog_post_id>/comments/", CommentListView.as_view(), name="comment-list"),
    path("comments/",include("comments.urls")),
    path("likes/",include("likes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)