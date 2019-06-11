from django.db import models


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    height = models.DateTimeField(auto_now=True)
    weight = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    speed = models.CharField(max_length=10)
    creDt = models.DateTimeField(auto_now=True)
