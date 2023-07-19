from django.db import models
from groups.models import Group,GroupMember
from django.utils.text import slugify
import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
from django import template

# Create your models here.
# posts.models.py file

User = get_user_model()
registration = template.Library()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)
    
    def __str__(self):
        return self.message
    
    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.get_username(),
                                              'pk':self.pk})
        
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']
        
    

