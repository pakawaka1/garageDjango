from rest_framework import serializers
from .models import Boat

class BoatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Boat
		fields = ('id', 'make', 'model', 'year', 'length', 'width', 'HIN', 'currentHours', 'serviceInterval', 'nextService')