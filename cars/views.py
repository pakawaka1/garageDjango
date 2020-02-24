from django.shortcuts import render
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

class CarView(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer