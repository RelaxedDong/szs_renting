# encodinig:utf-8
from django import views
from django.http import JsonResponse
from .models import House, Banner
from .serializers import HouseSerializer, BannerSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.db import connection
from api.utils import restful
import re
from api.utils import restful,word_check
from django.views import View


class AdminView(View):
    searchBar_regex = word_check.WordCheck().searchBar_regex
    @classmethod
    def wash_sql_parmas(cls, parm):
        """
        清洗sql参数，如果有不合格的参数，直接清洗为''
        """
        if isinstance(parm, str):
            match = cls.searchBar_regex.search(parm)
            if not match:
                return parm
            return ''

        if isinstance(parm, dict):
            _dict = {}
            for (k, v) in parm.items():
                if isinstance(v, str):
                    match = cls.searchBar_regex.search(v)
                    if match:
                        _dict[k] = ''
                    else:
                        _dict[k] = v
                elif isinstance(v, int):
                    _dict[k] = v
                elif isinstance(v, list):
                    new_lst = []
                    for row in v:
                        match = cls.searchBar_regex.search(row)
                        if not match:
                            new_lst.append(row)
                    _dict[k] = new_lst
                else:
                    _dict[k] = ''

            return _dict

        if isinstance(parm, list):
            _list = []
            for v in parm:
                if isinstance(v, str):
                    match = cls.searchBar_regex.search(v)
                    if match:
                        _list.append('')
                    else:
                        _list.append(v)
                else:
                    _list.append('')

            return _list

        return parm

class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认显示的个数
    default_limit = 10
    # 当前的位置
    offset_query_param = "offset"
    # 通过limit改变默认显示的个数
    limit_query_param = "limit"
    # 一页最多显示的个数
    max_limit = 10

class IndexView(AdminView):
    def get(self,request):
        houses = House.objects.get_queryset()
        banners = Banner.objects.all()
        pg = MyLimitOffsetPagination()
        page_roles = pg.paginate_queryset(queryset=houses, request=request)
        houses = HouseSerializer(page_roles, many=True).data
        for house in houses:
            house['facilities'] = re.findall(r'\'(.*?)\'', house['facilities'])
        banners_serializer = BannerSerializer(banners, many=True)
        return Response({'house': houses, 'banner': banners_serializer.data})




class SearchListView(AdminView):
    def get(self, request):
        args = self.wash_sql_parmas(request.GET)
        if request.method == "GET":
            cursor = connection.cursor()
            where = self.parse_form_data(args)
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
            house = HouseSerializer(house).data
            house['apartment'] = House.APARTMENT[int(house['apartment'])][1]
            imgs = re.findall(r'\'(.*?)\'', house.imgs)
            return restful.success(data={'house': house, 'imgs': imgs})
        except Exception as e:
            print(e)
            return restful.paramerror(msg="房源不存在")


