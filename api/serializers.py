from rest_framework import serializers

from .models import Present, Magaz, Product


class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'


class SerialazerPresent(serializers.Serializer):
    pass


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class ShopSerializer(serializers.ModelSerializer):
    prod = ProductSerializer(many=True)

    class Meta:
        model = Magaz
        fields = ['name', 'prod']
        depth = 1
