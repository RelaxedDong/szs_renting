# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 17:35
from django.db import models
from django.db.models import Manager
from django.utils import timezone
from api.house.models import House


class AccountManager(Manager):
    def create_user(self, openid, **kwargs):
        account = self.model(openid, **kwargs)
        account.save()
        return account


class AccountModel(models.Model):
    # objects = AccountManager()
    Gender = (('0', '未知'), ('1', '男'), ('2', '女'),)
    STATUS = (('1', '正常'), ('0', '冻结'),)
    openid = models.CharField("open id", max_length=30, unique=True, default=None, blank=True, null=True)
    nickname = models.CharField("微信昵称", max_length=50)
    avatarUrl = models.CharField('头像', max_length=255, blank=True)
    country = models.CharField('国家', max_length=30, blank=True)
    province = models.CharField('省份', max_length=30, blank=True)
    city = models.CharField('城市', max_length=30, blank=True)
    gender = models.CharField("性别", choices=Gender, default='0', max_length=1)
    status = models.CharField('状态', max_length=10, choices=STATUS, default='normal')
    name = models.CharField('真实姓名', max_length=30, default='', blank=True)
    create_time = models.DateTimeField('加入时间', default=timezone.now)

    class Meta:
        db_table = 'account'
        verbose_name = '账户'
        verbose_name_plural = '账户'


class CommentModel(models.Model):
    content = models.CharField(max_length=300, null=False, verbose_name="评论内容")
    create_time = models.DateTimeField('评论时间', default=timezone.now)
    house = models.ForeignKey(House, related_name="comments", verbose_name="房源", on_delete=models.CASCADE)
    author = models.ForeignKey(AccountModel, related_name="comments", on_delete=models.CASCADE)


class FavoriteModel(models.Model):
    create_time = models.DateTimeField('喜欢时间', default=timezone.now)
    house = models.ForeignKey(House, related_name="favorites", verbose_name="房源", on_delete=models.CASCADE)
    author = models.ForeignKey(AccountModel, related_name="favorites", on_delete=models.CASCADE)
