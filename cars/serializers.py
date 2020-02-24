from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Car
		fields = ('make', 'model', 'year', 'seats', 'color', 'VIN', 'currentMileage', 'serviceInterval', 'nextService')