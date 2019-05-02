# -*- coding: utf-8 -*-
from django.shortcuts import render

from team.models import List
from team.serializers import TeamSerializer
from rest_framework import viewsets

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = TeamSerializer
