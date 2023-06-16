from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView,View,ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from . import models
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'INJECTED DATA'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    template_name = 'basic_app/school_list.html'
    model = models.SchoolModel

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.SchoolModel
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    template_name = 'basic_app/school_form.html'
    fields = ('name','principal','location')
    model = models.SchoolModel

class SchoolUpdateView(UpdateView):
    template_name = 'basic_app/school_form.html'
    fields = ('name','principal')
    model = models.SchoolModel

class SchoolDeleteView(DeleteView):
    template_name = 'basic_app/school_confirm_delete.html'
    context_object_name = 'school'
    model = models.SchoolModel
    success_url = reverse_lazy('base:list')