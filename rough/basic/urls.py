from . import views
from django.urls import path

app_name = 'basic'

urlpatterns = [
    path('',views.Home.as_view(),name='index'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]