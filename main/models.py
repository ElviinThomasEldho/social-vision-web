from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

# class Impact(models.Model):
    
#     name = models.CharField(max_length=25,null=True)
#     desc = models.CharField(max_length=256000,null=True)
#     image1 = models.ImageField(null=True)
#     image2 = models.ImageField(null=True)
#     image3 = models.ImageField(null=True)
#     image4 = models.ImageField(null=True)

#     def __str__(self):
#         return (self.name)

class Event(models.Model):
    
    name = models.CharField(max_length=25,null=True)
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(null=True)
    image5 = models.ImageField(null=True)
    image6 = models.ImageField(null=True)
    image7 = models.ImageField(null=True)
    image8 = models.ImageField(null=True)
    image9 = models.ImageField(null=True)

    def __str__(self):
        return (self.name)

