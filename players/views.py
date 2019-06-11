# -*- coding: utf-8 -*-
from django.shortcuts import render

from players.models import List
from players.serializers import PlayersSerializer
from rest_framework import viewsets

from rest_framework import filters


# Create your views here.
class PlayersViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = PlayersSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'spped')
    ordering_fields = ('creDt',)
