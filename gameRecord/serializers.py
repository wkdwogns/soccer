from rest_framework import serializers

from gameRecord.models import Info


class gameRecordSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Info
        fields = ('id','gameType','startMember','startDt','creDt',)