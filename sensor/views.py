from .models import SensorData
from .serializers import SensorSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from sensor.permissions import IsOwnerOrReadOnly
import datetime as dt
from django.utils.decorators import method_decorator


class SensorDataView(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_last_week(self):
        time_delta = dt.datetime.now() - dt.timedelta(days=7)
        return SensorData.objects.exclude(date=time_delta).filter(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return SensorData.objects.all()

        return SensorData.objects.filter(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
