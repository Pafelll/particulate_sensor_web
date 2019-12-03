from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sensordata', views.SensorDataView)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]