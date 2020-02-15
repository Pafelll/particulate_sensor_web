from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView
from .models import SensorData

router = routers.DefaultRouter()
router.register('sensordatas', views.SensorDataView, base_name='SensorData')
router.register('user', views.UserViewSet, base_name='User')

urlpatterns = [
    path('api/', include(router.urls)),
    
    path('sensor/', TemplateView.as_view(template_name='sensor.html'))
]