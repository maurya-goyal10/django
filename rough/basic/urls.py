from . import views
from django.urls import path

app_name = 'basic'

urlpatterns = [
    path('',views.Home.as_view(),name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]