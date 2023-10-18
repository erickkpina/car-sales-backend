from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=120, default='')
    brand = models.CharField(max_length=120, default='')
    category = models.CharField(max_length=120, default='')
    gearbox = models.CharField(max_length=120, default='')
    fuel = models.CharField(max_length=120, default='')
    guarantee = models.CharField(max_length=120, default='')
    state_of_use = models.CharField(max_length=120, default='')
    year = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    cylinder_capacity = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    maximum_capacity = models.IntegerField(default=0)
    doors = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
