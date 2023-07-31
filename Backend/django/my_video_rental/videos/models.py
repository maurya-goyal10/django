from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    