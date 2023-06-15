from django.urls import path,re_path
from . import views
app_name = 'base'

urlpatterns = [
    path('schools_list/',views.SchoolListView.as_view(),name='list'),
    path('school/<int:pk>/',views.SchoolDetailView.as_view(),name='school_detail')
]