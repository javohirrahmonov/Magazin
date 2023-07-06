import rise as rise
from rest_framework import serializers
from .models import Suv, Mijoz, Admin, Haydovchi, Buyurtma

class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

    def validate_mijoz(self,qiymat):
        if qiymat.qarz  > 500000:
            raise serializers.ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        return qiymat