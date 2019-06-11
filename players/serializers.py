from rest_framework import serializers
from players.models import List
from django.utils import timezone


class PlayersSerializer(serializers.ModelSerializer): 

    class Meta:
        model = List
        fields = ('id','name','age','height','weight','position','speed')
