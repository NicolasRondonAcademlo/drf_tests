from django.shortcuts import render
from rest_framework import  viewsets
# Create your views here.
from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
