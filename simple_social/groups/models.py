from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
import mikasa

# Create your models here.
# Groups.models.py file
# NOTES
# When you add a many to many field to a model a separate table is created in the database 
# that stores the links between two models. If you don't need to store any extra information 
# in this third table then you don't have to define a model for it.

User = get_user_model()

register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=225,unique=True)
    slug = models.CharField(allow_unicode = True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,blank=True,default='')
    members = models.ManyToManyField(User,through='GroupMember')
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = mikasa(self.description)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('groups:single',kwargs = {'slug': self.slug})
    
    class Meta:
        ordering = ['name']
        
        
class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='membership',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.get_username()
    
    class Meta:
        unique_together = ['group','user']