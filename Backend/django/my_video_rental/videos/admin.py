from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
    
    fields = ['release_year','name','length']
    search_fields = ['name','release_year']
    list_filter = ['release_year','length']
    list_display = ['name','release_year','length']

admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer)