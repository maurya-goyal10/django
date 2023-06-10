from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def form(request):
    form = forms.BasicForm()

    if request.method == 'POST':
            form = forms.BasicForm(request.POST)
    
    if form.is_valid():
         print("Validation Completed ... ")
         print(f"NAME: {form.cleaned_data['name']}")
         print(f"EMAIL: {form.cleaned_data['email']}")
         print(f"TEXT: {form.cleaned_data['text']}")
    
    return render(request,'app1/forms.html',{'form': form})

