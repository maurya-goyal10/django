from django.shortcuts import render
from . import forms

from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are Logged in, Nice!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        form_user = forms.UserForm(data=request.POST)
        form_profile = forms.UserProfileInfoForm(data=request.POST)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = form_profile.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        
        else:
            print(form_user.errors,form_profile.errors)

    else:
        form_user = forms.UserForm()
        form_profile = forms.UserProfileInfoForm()
    
    return render(request,'basic_app/register.html',{'registered': registered,
                                                     'user_form': form_user,
                                                     'userprofile_form': form_profile})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account not active! ")
            
        else:
            print("Someone else tried to login and failed")
            return HttpResponse("Invalid login detials")
    else:
        return render(request,'basic_app/login.html')

            
    






