from django.urls import path,include
from team import views


urlpatterns = [
    path('', views.list),
]