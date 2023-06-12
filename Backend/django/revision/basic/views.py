from django.shortcuts import render
from basic import forms
from basic.models import Login

# Create your views here.
def index(request):
    return render(request,'basic/index.html')

def login(request):
    form = forms.LoginPage()

    if request.method == 'POST':
        form = forms.LoginPage(request.POST)
        
        if form.is_valid() :
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            obj = Login()
            obj.username = username
            obj.email =email
            obj.save()
            return render(request,'basic/index.html',{'success': 'yes','username': username})
    
    return render(request,'basic/login.html',{'form': form})


