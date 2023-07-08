from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect,HttpResponse
from blog.models import Post,Comment
from blog import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views.generic import (TemplateView,ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    
    def get_queryset(self):
        # - in order by indicates decreasing order
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['comments'] = Post.objects.get(pk=self.kwargs.get('pk')).comments.all().order_by('-create_date')
        return context

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    redirect_field_name = 'blog:post_detail'
    form_class = forms.PostForm
    model = Post
    
class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    redirect_field_name = 'blog:post_detail'
    form_class = forms.PostForm
    model = Post
    
class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    
class DraftListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    redirect_field_name = 'blog:post_detail'
    model = Post
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'drafts'
    
    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-create_date')
    
########################
########################

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)
    
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = forms.CommentForm()
        
    return render(request,'blog/comment_form.html',{'form': form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

###############################################
###############################################

def user_signup(request):
    registered = False
    
    if request.method == 'POST':
        form_user = forms.UserForm(request.POST)
        form_profile = forms.UserProfileForm(request.POST)
        
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            profile = form_profile.save(commit = False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            registered = True
            
        else:
            print(form_user.errors,form_profile.errors)
            
    else:
        form_user = forms.UserForm()
        form_profile = forms.UserProfileForm()
        
    return render(request,'registration/signup.html',{'registered': registered,
                            'form_user': form_user,
                            'form_profile': form_profile,
                            })
        
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:post_list'))
            
            else:
                return HttpResponse("User not active!!")
            
        else:
            return HttpResponse("Invalid Login!")
        
    else:
        return render(request,'registration/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:post_list'))

