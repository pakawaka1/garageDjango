from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'id')
        extra_kwargs = {'password': {'write_only': True}}
