from rest_framework import serializers

from .models import Zawod


class ZawodSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Zawod
        fields = '__all__'
        depth = 1
