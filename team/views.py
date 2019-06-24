# -*- coding: utf-8 -*-

from rest_framework import filters
from rest_framework import viewsets

from team.models import List
from team.serializers import TeamSerializer


# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'career')
    ordering_fields = ('creDt',)
