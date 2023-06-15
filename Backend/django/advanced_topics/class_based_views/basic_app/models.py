from django.db import models

# Create your models here.
class SchoolModel(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=512)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(SchoolModel,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name