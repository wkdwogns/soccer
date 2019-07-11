from django.db import models


# Create your models here.
class List(models.Model):
	team = models.IntegerField(null=True)
	name = models.CharField(max_length=50,null=True)
	age = models.CharField(max_length=10,null=True)
	height = models.DateTimeField(auto_now=True,null=True)
	weight = models.CharField(max_length=30,null=True)
	position = models.CharField(max_length=30,null=True)
	speed = models.CharField(max_length=10,null=True)
	creId = models.IntegerField(null=True)
	creDt = models.DateTimeField(auto_now=True,null=True)
