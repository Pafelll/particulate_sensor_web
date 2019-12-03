from .models import SensorData
from rest_framework import serializers
from django.contrib.auth.models import User


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('date', 'pm1', 'pm25', 'pm10', 'temperature', 'humidity', 'pressure', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    sensorname = serializers.PrimaryKeyRelatedField(many=True, queryset=SensorData.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sensorname')
