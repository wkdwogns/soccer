from django.urls import path,include
from team import views
from django.conf.urls import url

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]