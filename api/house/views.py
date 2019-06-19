# encodinig:utf-8
from django import views
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import House, Banner
from .serializers import HouseSerializer, BannerSerializer
from rest_framework.response import Response
from api.myuser.models import User
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import api_view
from django.db import connection


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
            house['facilities'] = list(eval(house['facilities']))
        banners_serializer = BannerSerializer(banners, many=True)
        return Response({'house': houses, 'banner': banners_serializer.data})


class SearchListView(views.View):
    def get(self, request):
        if request.method == "GET":
            cursor = connection.cursor()
            where = self.parse_form_data(request.GET)
            sql_str = """
                select title as title,price,subway from house_house 
                where status = '0' {condition}
            """.format(condition=where)
            print(sql_str)
            cursor.execute(sql_str)
            rows = cursor.fetchall()
            print(rows)
            return JsonResponse(data='ok', safe=False)

    def parse_form_data(self, cleaned_data):
        subway = cleaned_data.get("subway", "0")
        region = cleaned_data.get("region", "0")
        house_type = cleaned_data.get("house_type", "0")
        where = ""
        if subway != '0':
            where += """and subway = '%s' """ % subway if subway != "0" else ""

        if region != '0':
            where += """and region = '%s' """ % region if region != "0" else ""

        if house_type != '0':
            where += """and house_type = '%s' """ % house_type if house_type != "0" else ""
        return where
