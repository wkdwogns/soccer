# -*- coding: utf-8 -*-
from django.shortcuts import render

from player.models import List
from player.serializers import PlayerSerializer
from rest_framework import viewsets

from rest_framework import filters


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'spped')
    ordering_fields = ('creDt',)
