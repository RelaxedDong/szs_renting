#导入xamin模块
import xadmin
#导入School表
from .models import House,HouseImg,Banner

#创建注册类
class HouseAdmin(object):
    pass


#创建注册类
class HouseImgAdmin(object):
    pass


#创建注册类
class BannerAdmin(object):
    pass

xadmin.site.register(House, HouseAdmin)
xadmin.site.register(HouseImg, HouseImgAdmin)
xadmin.site.register(Banner, BannerAdmin)