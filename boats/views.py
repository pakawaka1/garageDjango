from django.shortcuts import render
from rest_framework import viewsets
from .models import Boat
from .serializers import BoatSerializer

class BoatView(viewsets.ModelViewSet):
	queryset = Boat.objects.all()
	serializer_class = BoatSerializer