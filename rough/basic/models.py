from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    BEGINER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    level_choices = (
        (BEGINER,'BEGINER'),
        (INTERMEDIATE,'INTERMEDIATE'),
        (ADVANCED,'ADVANCED')
    )
    level = models.IntegerField(
        choices=level_choices,
        default=BEGINER,
    )
    picture = models.ImageField(upload_to='profile_pics',blank = True)
    
    def __str__(self):
        return f"{self.user.username}"
    
    
