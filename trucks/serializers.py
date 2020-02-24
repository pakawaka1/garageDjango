from rest_framework import serializers
from .models import Truck

class TruckSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Truck
		fields = ('make', 'model', 'year', 'seats', 'bedLength', 'color', 'VIN', 'currentMileage', 'serviceInterval', 'nextService')