# encodinig:utf-8
from django import views
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import House, Banner
from .serializers import HouseSerializer, BannerSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import api_view
from django.db import connection
from api.utils import restful
import re


class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认显示的个数
    default_limit = 10
    # 当前的位置
    offset_query_param = "offset"
    # 通过limit改变默认显示的个数
    limit_query_param = "limit"
    # 一页最多显示的个数
    max_limit = 10


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        houses = House.objects.get_queryset()
        banners = Banner.objects.all()
        pg = MyLimitOffsetPagination()
        page_roles = pg.paginate_queryset(queryset=houses, request=request)
        houses = HouseSerializer(page_roles, many=True).data
        for house in houses:
            house['facilities'] = re.findall(r'\'(.*?)\'', house['facilities'])
        banners_serializer = BannerSerializer(banners, many=True)
        return Response({'house': houses, 'banner': banners_serializer.data})

class SearchListView(views.View):
    def get(self, request):
        if request.method == "GET":
            cursor = connection.cursor()
            where = self.parse_form_data(request.GET)
            sql_str = """
                select title,price,subway from house_house 
                where status = '0' {condition}
            """.format(condition=where)
            print(sql_str)
            res = cursor.execute(sql_str)
            print(res)
            return JsonResponse(data='ok', safe=False)

    def parse_form_data(self, cleaned_data):
        where = ""
        for key, value in cleaned_data.items():
            if key == 'title':
                where += """and title like '%s' """%('%'+value+'%')
            elif value != '0' and value != '不限':
                where += """and {key} = '%s' """.format(key=key) % value
        return where

class SelectItems(views.View):
    def get(self, request):
        subway = House.SUBWAY
        regions = House.REGION
        apartment = House.APARTMENT
        house_type = House.HOUSETYPE
        return JsonResponse({
            'subway': subway,
            'regions': regions,
            'apartment': apartment,
            'house_type': house_type,
        })


class HouseDetailView(views.View):
    def get(self,request,id):
        try:
            house = House.objects.get(pk=id)
            house.view_count += 2
            house.save()
            imgs = re.findall(r'\'(.*?)\'', house.imgs)
        except Exception as e:
            print(e)
            return restful.paramerror(msg="房源不存在")
        if house:
            house = HouseSerializer(house).data
            house['apartment'] = House.APARTMENT[int(house['apartment'])][1]
            return restful.success(data={'house':house,'imgs':imgs})
