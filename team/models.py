from django.db import models
from django.utils import timezone


class List(models.Model):
	name = models.CharField(max_length=50)
	career = models.TextField()
	creId = models.IntegerField(null=True)
	creDt = models.DateTimeField(auto_now=True)

