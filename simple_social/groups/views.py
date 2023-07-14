from typing import Any, Optional
from django import http
from django.shortcuts import render,get_object_or_404
from django.views import generic
from groups.models import Group,GroupMember
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib import messages

# Create your views here.
class CreateGroup(generic.CreateView):
    fields = ('name','description')
    model = Group
    
class SingleGroup(generic.DetailView):
    model  = Group
    context_object_name = 'group'
    
class ListGroups(generic.ListView):
    model = Group
    
class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        try:
            GroupMember.objects.create(user = self.request.user , group = group)
        except:
            messages.warning(self.request,"Warning! Already a member!")
        else:
            messages.success(self.request,"You are now a member")
            
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        try:
            membership = GroupMember.filter(
                user = self.request.user , 
                group__slug = self.kwargs.get('slug')).get()
        except:
            messages.warning(self.request,"Sorry! You're not a member of this group")
        else:
            membership.delete()
            messages.success(self.request,"You have left the group successfully")
            
        return super().get(request,*args,**kwargs)
