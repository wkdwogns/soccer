from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from gameRecord.models import Info

# Create your views here.
class gameRecord(APIView):
	def get(self, request, format=None):        
		
		return Response(Info.objects.all())