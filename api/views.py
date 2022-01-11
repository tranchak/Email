from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Present, Magaz
from .serializers import PresentSerializer, ShopSerializer


@api_view(["GET", "POST"])
def get_presente(request):
    all_presente = Present.objects.all()
    serialise = PresentSerializer(all_presente, many=True)
    #print(serialise.data)
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