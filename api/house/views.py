#encodinig:utf-8
from django import views
from .serializers import HouseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import House

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        houses = House.objects.all()
        serializer = HouseSerializer(houses)
        return Response(serializer.data)



