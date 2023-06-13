from . import views
from django.urls import path,re_path

# Templating
app_name = 'base'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
]