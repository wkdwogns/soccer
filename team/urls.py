from django.urls import path, include
from rest_framework import routers

from team import views

router = routers.DefaultRouter()
router.register(r'', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]