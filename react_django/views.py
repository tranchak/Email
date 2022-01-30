from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from react_django.models import Car
from react_django.serializers import CarSer


class CarViewSet(viewsets.ViewSet):
    def list (self, request):
        cars=Car.objects.all()
        serializer=CarSer(cars, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cars = Car.objects.all()
        car = get_object_or_404(cars, pk=pk)
        serializer = CarSer(car)
        return Response(serializer.data)