from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    
    def __str__(self):
        return self.title
    
