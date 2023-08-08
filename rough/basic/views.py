from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from . import models,forms

# Create your views here.
class Home(TemplateView):
    template_name = 'basic/home.html'
    
class SignUp(CreateView):
    form_class = forms.UserProfileForm
    model = models.UserProfile
    template_name = 'basic/signup.html'
