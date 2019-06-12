from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class House(models.Model):
    STATUS = (
        ('1','售卖中'),
        ('2','已删除'),
        ('3','已售卖'),
    )
    title = models.CharField(max_length=150,null=False,blank=False,verbose_name="标题")
    price = models.IntegerField(null=False,blank=False,verbose_name="价格")
    cover = models.CharField(max_length=200,verbose_name="封面")
    desc = models.TextField(verbose_name="详情")
    address = models.CharField(max_length=150,verbose_name="地址")
    facilities = models.TextField(default={},null=False,verbose_name="设施")
    is_elevator = models.BooleanField(default=False,verbose_name="电梯房")
    has_living_room = models.BooleanField(default=False,verbose_name="客厅房")
    status = models.CharField(choices=STATUS,default='1',max_length=1,verbose_name="状态")
    publisher = models.ForeignKey(get_user_model(),on_delete=models.PROTECT,verbose_name='发布者')

    def __repr__(self):
        return "%s %s"%self.id,self.title

class HouseImg(models.Model):
    STATUS = (
        ('1','展示中'),
        ('2','未展示'),
        ('3','已删除'),
    )
    House_id = models.ForeignKey("House",on_delete=models.PROTECT,verbose_name="房源")
    cover = models.CharField(max_length=200,verbose_name="图片")
    url = models.CharField(max_length=200,verbose_name="跳转链接")
    status = models.CharField(choices=STATUS, default='1', max_length=1, verbose_name="状态")


class Banner(models.Model):
    img_url = models.CharField(max_length=200,null=False,verbose_name="封面图")
    redirect_url = models.CharField(max_length=200,null=False,verbose_name="跳转链接")
    publisher = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='发布者')
    desc = models.CharField(max_length=200,default="",null=True,verbose_name="说明")
    create_time = models.DateTimeField(default=timezone.now,verbose_name="加入时间")