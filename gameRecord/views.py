from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from gameRecord.models import Info
from gameRecord.serializers import gameRecordSerializer


# Create your views here.
class gameRecord(APIView):

	def get(self, request, format=None):
		rs = Info.objects.all()       	
		serializer = gameRecordSerializer(rs,many=True)
		return Response(serializer.data)
		# return JsonResponse(serializer.data,safe=False)

	def post(self,request,format=None):
		data = JSONParser().parse(request)
		serializer = gameRecordSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)