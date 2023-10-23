from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Category, Gearbox, Fuel, StateOfUse, Brand, CarModel, Car, CarImage

# Register your models here.

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # Number of empty forms to display for adding images

class CarAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'brand', 'car_model', 'category', 'gearbox', 'fuel', 'guarantee', 'state_of_use', 'year', 'mileage', 'cylinder_capacity', 'power', 'maximum_capacity', 'doors', 'price',)
    inlines = [CarImageInline]

admin.site.register(Category)
admin.site.register(Gearbox)
admin.site.register(Fuel)
admin.site.register(StateOfUse)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage)
