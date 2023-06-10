from basic_app import views
from django.urls import path,re_path

## Used for relative templating
app_name = 'basic'

urlpatterns = [
    re_path(r'^$',views.base,name='base'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]