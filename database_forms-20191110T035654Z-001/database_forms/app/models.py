from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=30, default="India")
    diet = models.IntegerField(default=0)
    car_fuel = models.IntegerField(default=0)
    scooter = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    footprint = models.FloatField(default=0)
    journey_time = models.IntegerField(default=0)
    time = models.FloatField(default=0)
    meal = models.FloatField(default=0)
    shop = models.IntegerField(default=0)
    compost = models.IntegerField(default=0)
    solar = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    ct = models.IntegerField(default=0)
    cn = models.IntegerField(default=0)
    bun = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username
