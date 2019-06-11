# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 19:53
from django.http import JsonResponse


class StatuCode(object):
    ok = 200
    error = 400
    internet_error = 500


def success(code=StatuCode.ok, msg="ok", data=""):
    return JsonResponse({"code": code, 'msg': msg, 'data': data})


def paramerror(code=StatuCode.error, msg="error", data=""):
    return JsonResponse({"code": code, 'msg': msg, 'data': data})


def server_error(code=StatuCode.internet_error, msg="internet rerror", data=None):
    return JsonResponse({"code": code, 'msg': msg, 'data': data})