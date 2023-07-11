from django.shortcuts import render
from django.views import generic
from groups.models import Group,GroupMember
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.
class CreateGroup(generic.CreateView):
    fields = ('name','description')
    model = Group
    
class SingleGroup(generic.DetailView):
    model  = Group
    context_object_name = 'group'
    
class ListGroups(generic.ListView):
    model = Group