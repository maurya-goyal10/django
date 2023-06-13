from django.urls import path
from basic_app import views

app_name = 'base'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('special/',views.special,name='special')

]