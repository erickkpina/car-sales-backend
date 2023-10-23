from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        # Optionally, you can prefetch related images to optimize the query
        queryset = queryset.prefetch_related('carimage_set')
        return queryset
