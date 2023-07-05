from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from blog.models import Post,Comment
from blog import forms
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        # - in order by indicates decreasing order
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    
class PostDetailView(DetailView):
    model = Post
    
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = Post
    
class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = Post
    
class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog.post_list')
    
class DraftListView(LoginRequiredMixin,ListView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(publish_date_isnull=True).order_by('-create_date')
    
    
