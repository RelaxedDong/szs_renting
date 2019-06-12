#encodinig:utf-8
from django import views
from .models import House
from .serializers import HouseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        houses = House.objects.all()
        serializer = HouseSerializer(houses,many=True)
        return Response(serializer.data)



