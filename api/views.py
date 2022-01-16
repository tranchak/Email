from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Present, Magaz, Product
from .serializers import PresentSerializer, ShopSerializer, ProductSerializer


@api_view(["GET", "POST"])
def get_presente(request):
    all_presente = Present.objects.all()
    serialise = PresentSerializer(all_presente, many=True)
    # print(serialise.data)
    if request.method == "POST":
        print(request.data)
        serialise = PresentSerializer(data=request.data)
        serialise.is_valid()
        print(serialise.validated_data)
        serialise.save()
    return Response({'message': serialise.data})


@api_view(['GET', 'POST'])
def all_shop(request, id):
    shop = Magaz.objects.filter(id=id)
    serialise = ShopSerializer(shop, many=True)
    return Response(serialise.data)


@api_view(['GET', 'POST'])
def all_mag(request):
    mag = Magaz.objects.all()
    serialise = ShopSerializer(mag, many=True)
    if request.method == 'POST':
        serialise = ShopSerializer(data=request.data)
        if serialise.is_valid():
            serialise.save()
            return Response({serialise.data})
    else:
        return Response(serialise.data)


@api_view
def all_product(request):
    prod = Product.objects.all()
    serialiser = ProductSerializer(prod, many=True)
    return Response(serialiser.data)
