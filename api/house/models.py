from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from DjangoUeditor.models import UEditorField


# Create your models here.
class HouseManager(models.Manager):
    pass


class House(models.Model):
    STATUS = (('0', '售卖中'), ('1', '已删除'), ('2', '已售卖'),)
    SUBWAY = (
        ('0', '不限'), ('1', '1号线'), ('2', '2号线'), ('3', '3号线'), ('4', '4号线'), ('5', '5号线'), ('6', '6号线'),
        ('7', '7号线'), ('8', '8号线'), ('9', '9号线'), ('10', '10号线'), ('11', '11号线'),)
    REGION = (
        ('0', '不限'), ('1', '罗湖区'), ('2', '福田区'), ('3', '南山区'), ('4', '龙岗区'), ('5', '盐田区'),
        ('6', '宝安区'), ('7', '光明新区'), ('8', '坪山新区'), ('9', '龙华新区'), ('10', '大鹏新区'),)
    APARTMENT = (('0', '不限'), ('1', '单间'), ('2', '合租'), ('3', '一室一厅'), ('4', '两室一厅'), ('5', '其它'))
    HOUSETYPE = (('0', '不限'), ('1', '整租'), ('2', '合租'))
    objects = HouseManager
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="标题")
    price = models.IntegerField(null=False, blank=False, verbose_name="价格")
    area = models.IntegerField(null=False, verbose_name="面积")
    storey = models.CharField(max_length=3, null=False, verbose_name="楼层")
    cover = models.CharField(max_length=200, verbose_name="封面")
    desc = UEditorField(verbose_name="详情", imagePath="images/ueditor/", filePath="images/ueditor/")
    address = models.CharField(max_length=150, verbose_name="详细地址")
    subway = models.CharField(max_length=20, choices=SUBWAY, verbose_name="周边地铁", null=False, default='0')
    region = models.CharField(max_length=20, choices=REGION, verbose_name="区域", null=False, default='0')
    house_type = models.CharField(max_length=20, choices=HOUSETYPE, default='0', null=False, verbose_name='类型（整租，合租）')
    apartment = models.CharField(max_length=20, verbose_name="户型", choices=APARTMENT, default='0')
    facilities = models.TextField(default={}, null=False, verbose_name="设施")
    is_elevator = models.BooleanField(default=False, verbose_name="电梯房")
    is_apartment = models.BooleanField(default=False, verbose_name="公寓房")
    status = models.CharField(choices=STATUS, default='0', max_length=1, verbose_name="状态")
    publisher = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='发布者')

    def __repr__(self):
        return "%s %s" % self.id, self.title

    class Meta:
        verbose_name = '房源'
        verbose_name_plural = '房源'


class HouseImg(models.Model):
    STATUS = (
        ('1', '展示中'),
        ('2', '未展示'),
        ('3', '已删除'),
    )
    House_id = models.ForeignKey("House", on_delete=models.PROTECT, verbose_name="房源")
    cover = models.CharField(max_length=200, verbose_name="图片")
    url = models.CharField(max_length=200, verbose_name="跳转链接")
    status = models.CharField(choices=STATUS, default='1', max_length=1, verbose_name="状态")

    class Meta:
        verbose_name = '房源图片'
        verbose_name_plural = '房源图片'


class Banner(models.Model):
    img_url = models.CharField(max_length=200, null=False, verbose_name="封面图")
    redirect_url = models.CharField(max_length=200, null=False, verbose_name="跳转链接")
    publisher = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='发布者')
    desc = models.CharField(max_length=200, default="", null=True, verbose_name="说明")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="加入时间")

    class Meta:
        verbose_name = '首页banner'
        verbose_name_plural = '首页banner'
