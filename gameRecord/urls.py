from django.urls import path, include
from rest_framework import routers

from gameRecord.views import gameRecord

urlpatterns = [
    path('list/', gameRecord.as_view() ),
]