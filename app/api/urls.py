from django.urls import path, re_path
from rest_framework import permissions
from .views import TemperatureAPIView


urlpatterns = [
    path('locations/<str:city>/', TemperatureAPIView.as_view(),
         name='weather-stats'),
]
