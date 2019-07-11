# -*- coding: utf-8 -*-

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from team.models import List
from team.serializers import TeamSerializer

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend,)
    filterset_fields = ('name', 'career','creId',)
    search_fields = ('name', 'career')
    ordering_fields = ('creDt',)

    @action(detail=False, methods=['get'])
    def get_myTeam(self, requests):
        pk = requests.user.pk
        return Response(List.objects.filter(creId=pk))
