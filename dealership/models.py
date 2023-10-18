from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    price = models.IntegerField()

    def _str_(self):
        return self.name