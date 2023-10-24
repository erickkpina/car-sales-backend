from rest_framework import serializers
from .models import Car, CarImage, Category, Gearbox




class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ('img',)

class CarSerializer(serializers.ModelSerializer):
    carimage_set = CarImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name')
    gearbox = serializers.CharField(source='gearbox.name')
    brand = serializers.CharField(source='brand.name')
    car_model = serializers.CharField(source='car_model.name')
    fuel = serializers.CharField(source='fuel.name')
    state_of_use = serializers.CharField(source='state_of_use.name')
    class Meta:
        model = Car
        fields = '__all__'
