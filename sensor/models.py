from django.db import models
from crum import get_current_user


class SensorData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pm1 = models.IntegerField()
    pm25 = models.IntegerField()
    pm10 = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='measure_id', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date.strftime("%d-%b-%Y %H:%M"))
