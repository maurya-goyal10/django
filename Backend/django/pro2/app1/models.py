from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    text = models.CharField(max_length=512)

    def __str__(self):
        return self.name+": "+self.email
