from django.urls import path, include
from rest_framework import routers

from players import views

router = routers.DefaultRouter()
router.register(r'', views.PlayersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]