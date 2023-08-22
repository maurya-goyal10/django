from typing import Any, Dict
from django import http
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView,CreateView
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
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
    
def user_login(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basic:index'))
            
            else:
                message = "ACCOUNT EXPIRED"
                return render(request,'basic/login.html',{'message': message})

        else:
            message = "INVALID LOGIN"
            return render(request,'basic/login.html',{'message': message})
            
    else:
        return render(request,'basic/login.html',{'message': message})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic:index'))
    
                
                