from .models import SensorData
from rest_framework import serializers
from django.contrib.auth.models import User


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'date', 'pm1', 'pm25', 'pm10', 'temperature', 'humidity', 'pressure', 'owner')
        owner = serializers.ReadOnlyField(source='owner.owner')


class UserSerializer(serializers.ModelSerializer):
    measure_id = serializers.PrimaryKeyRelatedField(many=True, queryset=SensorData.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'measure_id')
