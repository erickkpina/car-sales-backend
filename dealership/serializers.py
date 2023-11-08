from rest_framework import serializers
from .models import Car, CarImage, Category, Gearbox, Brand
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'