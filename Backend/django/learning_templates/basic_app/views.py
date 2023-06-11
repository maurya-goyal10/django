from django.shortcuts import render

# Create your views here.
def index(request):
    text = "hello world"
    number = 100
    my_dict = {
        'text': text,
        'number': number
    }
    return render(request,'basic_app/index.html',my_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_template.html')