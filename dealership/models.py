from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Gearbox(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Fuel(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name
class StateOfUse(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"

class Car(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gearbox = models.ForeignKey(Gearbox, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    guarantee = models.CharField(max_length=120, default='')
    state_of_use = models.ForeignKey(StateOfUse, on_delete=models.CASCADE)
    year = models.IntegerField()
    mileage = models.IntegerField()
    cylinder_capacity = models.IntegerField()
    power = models.IntegerField()
    maximum_capacity = models.IntegerField()
    doors = models.IntegerField()
    price = models.IntegerField()
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car_model.brand.name} {self.car_model.name} - {self.plate_number}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def get_upload_path(instance, filename):
        # Generate upload path dynamically based on the plate variable
        return f'car/{instance.car.plate_number}/{filename}'

    img = models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return f"Image for {self.car.car_model.brand.name} {self.car.car_model.name} - {self.car.plate_number}"



"""
class Vehicle (models.Model):
    plate = models.CharField(max_length=120, default='')
    def get_upload_path(instance, filename):
        # Generate upload path dynamically based on the plate variable
        return f'car/{instance.plate}/{filename}'

    img = models.ImageField(upload_to=get_upload_path)
"""