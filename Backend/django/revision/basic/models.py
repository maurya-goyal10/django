from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=256,unique=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.username + ": " + self.email