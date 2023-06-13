from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserProfileInfo(models.Model):
    # we make one to one fields and don't inherit it
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # other attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username