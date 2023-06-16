from django.urls import path,re_path
from . import views
app_name = 'base'

urlpatterns = [
    path('schools_list/',views.SchoolListView.as_view(),name='list'),
    path('school/<int:pk>/',views.SchoolDetailView.as_view(),name='school_detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update_school/<int:pk>/',views.SchoolUpdateView.as_view(),name='school_update'),
    path('delete_school/<int:pk>/',views.SchoolDeleteView.as_view(),name='school_delete'),
]