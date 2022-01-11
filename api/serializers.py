from rest_framework import serializers

from .models import Present, Magaz


class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'


class SerialazerPresent(serializers.Serializer):
    pass


class ShopSerializer(serializers.ModelSerializer):
    prod = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = Magaz
        fields = ['name', 'prod']
        depth = 1
