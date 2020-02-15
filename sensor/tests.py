from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import SensorData
from .serializers import SensorSerializer
import json
from django.contrib.auth.models import User


class SensorDataViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_measure(pm1='', pm25='', pm10='', temperature='', humidity='', pressure=''):
        if pm1 != '' and pm25 != '' and pm10 != '' and temperature != '' and humidity != '' and pressure != '':
            SensorData.objects.create(pm1=pm1, pm25=pm25, pm10=pm10, temperature=temperature,
                                      humidity=humidity, pressure=pressure)

    def login_as_user(self, username='', password=''):
        url = reverse("auth-login", kwargs={"version": "v1"})
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="admin",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        self.create_measure("10", "25", "34", "1", "45", "999")
        self.create_measure("45", "5", "9", "-6.1", "54", "1002")
        self.create_measure("6", "2", "6", "1.5", "35", "1001")
        self.create_measure("3", "7", "50", "-30", "60", "1003")


class GetAllMeasuresTest(SensorDataViewTest):

    def test_get_all_measures(self):
        request = APIRequestFactory()
        response = self.client.get(reverse("api/sensordatas/", kwargs={"version": "v1"}))
        expected = SensorData.objects.all()
        serialized = SensorSerializer(expected, many=True)
