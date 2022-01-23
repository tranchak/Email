from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Magaz
from .models import Zawod
from .serializers import ZawodSerialiser


class ZawodList(APIView):
    def get(self, request, format=None):
        zaw = Zawod.objects.all()
        serializer = ZawodSerialiser(zaw, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ZawodSerialiser(data=request.data)
        if serializer.is_valid():
            zawod = serializer.validated_data.get('name')
            adr = serializer.validated_data.get('address')
            if Zawod.objects.filter(name=zawod).filter(address=adr).exists():
                return Response('ОШИБКА 400!!! Есть такое!')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateZawod(ListAPIView):
    serializer_class = ZawodSerialiser

    def get_queryset(self):
        return Zawod.objects.filter(name='МАЗ')


class ZawodDetail(viewsets.ViewSet):
    queryset = Zawod.objects.all()
    def list(self, request):
        queryset = Zawod.objects.all() #filter(name='МАЗ')
        serialise = ZawodSerialiser(queryset, many=True)
        return Response(serialise.data)

    def retrieve(self, request, pk=None):
        queryset = Zawod.objects.all()
        zaw_ok = get_object_or_404(queryset, pk=pk)
        serialise = ZawodSerialiser(zaw_ok)
        return Response(serialise.data)

class StartViewSet(viewsets.ModelViewSet):
    queryset = Zawod.objects.all()
    serializer_class = ZawodSerialiser