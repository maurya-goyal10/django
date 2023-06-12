from django.urls import path,re_path
from basic import views

app_name = 'basic'

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    path('login/',views.login,name='login')
]