from django.db import models

# Create your models here.

class Info(models.Model):
	gameType = models.IntegerField()
	startMember = models.TextField()
	startDt = creDt = models.DateTimeField()
	creDt = models.DateTimeField(auto_now=True)

class History(models.Model):
	actionType = [
	    ('FR', 'Freshman'),
	    ('SO', 'Sophomore'),
	    ('JR', 'Junior'),
	    ('SR', 'Senior'),
	]
	player = models.IntegerField(null=False)
	action = models.CharField(max_length=2,choices=actionType,default='FR')
