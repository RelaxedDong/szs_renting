#导入xamin模块
import xadmin
#导入School表
from .models import House,HouseImg,Banner

#创建注册类
class HouseAdmin(object):
    list_display = ['title', 'price', 'cover', 'subway', 'region']  # 显示的字段
    search_fields = ['title', 'subway', 'region', 'price']  # 搜索
    list_filter = ['title', 'price', 'subway', 'region']  # 过滤
    style_fields = {"desc": "ueditor"}
    model_icon = 'fa fa-list'


#创建注册类
class HouseImgAdmin(object):
    model_icon = 'fa fa-image'



#创建注册类
class BannerAdmin(object):
    list_display = ['img_url','desc', 'create_time', 'publisher']  # 显示的字段
    search_fields = ['create_time', 'publisher']    # 搜索
    list_filter = ['create_time', 'publisher']  # 过滤
    model_icon = 'fa fa-square'




xadmin.site.register(House, HouseAdmin)
xadmin.site.register(HouseImg, HouseImgAdmin)
xadmin.site.register(Banner, BannerAdmin)