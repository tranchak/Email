from rest_framework import serializers

from react_django.models import Car

class CarSer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'