from rest_framework import serializers
from .models import Car, CarImage

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ('img',)

class CarSerializer(serializers.ModelSerializer):
    carimage_set = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
