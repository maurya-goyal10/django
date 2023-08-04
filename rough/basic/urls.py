from . import views
from django.urls import path

app_name = 'basic'

urlpatterns = [
    path('',views.Home.as_view(),name='index'),
]