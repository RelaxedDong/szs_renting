#encoding:utf-8
from rest_framework import serializers
from .models import House

# Serializers define the API representation.

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('title','price')