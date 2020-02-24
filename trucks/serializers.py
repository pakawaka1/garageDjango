from rest_framework import serializers
from .models import Truck

class TruckSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Truck
		fields = ('id', 'make', 'model', 'year', 'seats', 'bedLength', 'color', 'VIN', 'currentMileage', 'serviceInterval', 'nextService')