from rest_framework import serializers
from .models import Auth

class AuthSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Auth
		fields = ('name', 'email')