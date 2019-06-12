#encoding:utf-8
from .models import House
from rest_framework import serializers

# Serializers define the API representation.

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'