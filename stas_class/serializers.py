from rest_framework import serializers

from .models import Zawod


class ZawodSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Zawod
        fields = ['name', 'address']
        # depth = 1
