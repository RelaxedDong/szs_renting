#导入xamin模块
import xadmin
#导入School表
from .models import House,HouseImg

#创建注册类
class HouseAdmin(object):
    pass


#创建注册类
class HouseImgAdmin(object):
    pass

xadmin.site.register(House, HouseAdmin)
xadmin.site.register(HouseImg, HouseImgAdmin)