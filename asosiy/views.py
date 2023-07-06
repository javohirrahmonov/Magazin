from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from .models import *
from .serializers import *


class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brend']
    ordering_fields = ['narx']

class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism','tel']
    ordering_fields = ['qarz']

class BuyurtmaAPIView(APIView):
    def get(self,request):
        buyurtmalar = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtmalar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(data = buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminlarAPIView(APIView):
    def get(self,request):
        adminlar = Admin.objects.all()
        serializer = AdminSerializer(adminlar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminDetalAPIView(APIView):
    def get(self,request,pk):
        admin = Admin.objects.get(id = pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HaydovchilarAPIView(APIView):
    def get(self,request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HaydovchiDetalAPIView(APIView):
    def get(self,request,pk):
        haydovchi = Haydovchi.objects.get(id = pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data, status=status.HTTP_200_OK)