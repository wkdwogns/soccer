from django.db import models
from django.utils import timezone


class TeamList(models.Model):
	name = models.CharField(max_length=50)
	career = models.TextField()
	creDt = models.DateTimeField(default=timezone.now)

