from rest_framework import serializers,viewsets
from team.models import List


class TeamSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    career = serializers.CharField(style={'base_template': 'textarea.html'})
    creDt = serializers.DateTimeField(required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return List.objects.create(**validated_data)

    class meta:
        ordering='creDt'
