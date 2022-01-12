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
        # print(request.data)
        serialise_shop = ShopSerializer(data=request.data)
        print(serialise_shop)
        # serialise_product = ProductSerializer(data=request.data.get('prod'))
        if serialise_shop.is_valid():
            shop = serialise_shop.validated_data.get('name')
            prot = serialise_shop.validated_data.get('prod')
            # print(shop, '1--')
            print(prot, '2--')
            if Magaz.objects.filter(name=shop).exists():
                return Response({'massage': 'ERRRRRROR. Ошибка есть такой магазин'})
            else:
                Magaz.objects.create(name=shop)
                z = Magaz.objects.get(name=shop)
                print(z)
                for p in prot:
                    Product.objects.create(name=p, magaz_id=z.id)
                    print(p)
            return Response(serialise.data)
        return Response(serialise_shop.errors)
    return Response(serialise.data)
