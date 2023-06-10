from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def signup(request):
    form = forms.SignUp()

    if request.method == 'POST':
        form = forms.SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'app1/index.html',{'name': form.cleaned_data['name']})
    
    return render(request,'app1/signup.html',{'form':form})