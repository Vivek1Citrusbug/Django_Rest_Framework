from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost
from comments.models import UserComments
from .forms import BlogPostForm
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from blogs.serializers import BlogListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from blogs.general import MyPaginator

class BlogPostListingAPIView(ModelViewSet):
    serializer_class = BlogListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['likes']
    # pagination_class = MyPaginator   # Used custom pagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return BlogPost.objects.all()
    
# class CommentListAPIView(ListAPIView):
#     serializer_class = BlogPostWithComments

#     def get_queryset(self):
#         blog_post_id = self.kwargs['blog_post_id']
#         return UserComments.objects.filter(post_id=blog_post_id)
    

class BlogPostListingView(LoginRequiredMixin, ListView):
    """This view is used to list all the blogs"""

    model = BlogPost
    template_name = "blogs/blog_list.html"
    context_object_name = "posts"
    ordering = ["-date_published"]


class BlogDetailView(LoginRequiredMixin, DetailView):
    """This view is used to give detail of selected blog"""

    model = BlogPost
    template_name = "blogs/blog_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["likes_count"] = post.likes.count()
        context["user_liked"] = post.likes.filter(
            user=self.request.user
        ).exists()  
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    """This view is used to create new blog"""

    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This view is used to update existing blog"""

    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """This view is used to delete existing blog"""

    model = BlogPost
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blog_list")
    context_object_name = "post"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user or self.request.user.is_staff
