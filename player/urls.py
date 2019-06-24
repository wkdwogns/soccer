from django.urls import path, include
from rest_framework import routers

from player import views

router = routers.DefaultRouter()
router.register(r'', views.PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]