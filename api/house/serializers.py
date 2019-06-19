#encoding:utf-8
from .models import House,Banner
from rest_framework import serializers

# Serializers define the API representation.


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'