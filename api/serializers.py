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

    def create(self, validated_data):
        proda = validated_data.pop('prod')
        magazins = Magaz.objects.create(**validated_data)
        for i in proda:
            Product.objects.create(magazins=magazins, **i)
        return magazins
