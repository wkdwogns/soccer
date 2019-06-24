from rest_framework import serializers
from player.models import List
from django.utils import timezone


class PlayerSerializer(serializers.ModelSerializer): 

    class Meta:
        model = List
        fields = ('id','team','name','age','height','weight','position','speed')
