from django.db import models

# Create your models here.

class Info(models.Model):
	gameType = models.IntegerField()
	startMember = models.TextField()
	startDt = models.DateTimeField()
	otherTeamNm = models.CharField(null=True,max_length=50)
	creDt = models.DateTimeField(auto_now=True)

class History(models.Model):
	actionType = [
	    

	    ('0200', '포메이션 변경'),
	    ('0201', '4-4-2'),
	    ('0202', '3-5-2'),
	    ('0203', '4-2-3-1'),
	    ('0204', '4-3-3'),
	    ('0205', '5-4-1'),
	    ('0206', '4-5-1'),

	    ('0300', '선수 교체'),

	    ('0400', '필드골'),
	    ('0401', 'pk골'),
	    ('0402', '프리킥골'),
	    ('0403', '어시스트'), 
	    ('0404', '슈팅'),
	    ('0405', '유효슈팅'),
	    ('0406', '크로스'),
	    ('0407', '헤더'),
	    ('0408', '공간침투'),
	    ('0409', '공간패스'),
	    ('0410', '선방'),
	    
	    ('0500', '컨트롤미스'),
	    ('0501', '패스미스'),
	    ('0502', '체력저하'),

		('0600', '파울'),
	    ('0601', '옐로카드'),
	    ('0602', '레드카드'),
	]
	player = models.IntegerField(null=False)
	action = models.CharField(null=False,max_length=4,choices=actionType,default='')
	before = models.CharField(null=True,max_length=30)
	after = models.CharField(null=True,max_length=30)
