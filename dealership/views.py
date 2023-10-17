from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializer
from .models import Car


# Create your views here.

class CarView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
