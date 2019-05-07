from rest_framework import serializers
from team.models import List
from django.utils import timezone


class TeamSerializer(serializers.ModelSerializer): 
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=50)
    # career = serializers.CharField(style={'base_template': 'textarea.html'})
    # creDt = serializers.DateTimeField()
    class Meta:
        model = List
        fields = ('id','name','career')


    def create(self, validated_data):
        """
        Create and return a new `List` instance, given the validated data.
        """
        return List.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `List` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.career = validated_data.get('career', instance.career)
        instance.creDt = validated_data.get('creDt', instance.creDt)
        instance.save()
        return instance
    
