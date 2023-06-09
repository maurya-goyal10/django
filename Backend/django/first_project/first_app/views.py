from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Webpage,Topic

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hi i am loading the template in first_app/index.html"}
    return render(request,'first_app/index.html',context=my_dict)

def access_record(request):
    record_list = AccessRecord.objects.order_by('date')
    my_dict = {'records': record_list}
    return render(request,'first_app/access_record.html',context=my_dict)