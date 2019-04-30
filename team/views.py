# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from team.models import List
from team.serializers import TeamSerializer

# Create your views here.

@csrf_exempt
def list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        team = List.objects.all()

        serializer = TeamSerializer(team, many=True)

        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
