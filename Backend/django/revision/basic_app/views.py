from django.shortcuts import render
from basic_app import forms

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Can only take place if logged in")

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        userprofile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            user_profile = userprofile_form.save(commit=False)
            user_profile.user = user
            if request.FILES.get('profile_pic'):
                user_profile.profile_pic = request.FILES['profile_pic']
            user_profile.save()

            registered = True
    
    else:
        user_form = forms.UserForm()
        userprofile_form = forms.UserProfileForm()

    return render(request,'basic_app/register.html',{'registered': registered,
                                                     'user_form': user_form,
                                                     'userprofile_form': userprofile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                
            else:
                return HttpResponse("Please reactivate your account!")

        else:
            return HttpResponse("Invalid userdetails!!")

    return render(request,'basic_app/login.html')

