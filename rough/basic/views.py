from typing import Any, Dict
from django import http
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from . import models,forms

# Create your views here.
class Home(TemplateView):
    template_name = 'basic/home.html'
    
def signup(request):
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password('password')
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        
        else:
            print(user_form.errors.as_text() + profile_form.errors.as_text)
            
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileForm()
    
    return render(request,'basic/signup.html',{'registered': registered,
                                               'form': user_form,
                                               'profile_form': profile_form})
            
            
            
            

        
        
        
        
  