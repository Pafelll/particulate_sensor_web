from django.shortcuts import render
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from sensor.permissions import IsOwnerOrReadOnly


class SensorDataView(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
