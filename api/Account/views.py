#encoding:utf-8
from django.http import JsonResponse
from django.conf import settings
from .models import Account
from django import views
import requests,json
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class UserLoginView(views.View):
    def post(self,request):
        data = request.POST
        code = data.get("code", None)
        if code:
            appid = settings.WXSETTINGS.get("APP_ID")
            app_secret = settings.WXSETTINGS.get("APP_SECRET")
            url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
                .format(appid, app_secret, code)
            r = requests.get(url)
            res = json.loads(r.text)
            openid = res['openid'] if 'openid' in res else None
            if not openid:
                return JsonResponse({"msg": "openid 失败"})
            try:
                user = Account.objects.get(openid=openid)
            except Exception:
                nickName = data.get("nickName",'')
                gender = data.get("gender",'')
                avatarUrl = data.get("avatarUrl",'')
                province = data.get("province",'')
                city = data.get("city",'')
                user = Account.objects.create(
                    nickname=nickName,avatarUrl=avatarUrl, province=province,
                    city=city,gender=gender, openid=openid
                )
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return JsonResponse({
                    "user_id": user.id,
                    "nickname": user.nickname,
                    "avatar": user.avatarUrl,
                    "token": token,
                    })
        else:
            return JsonResponse({"msg": "code未传递"})

    def get(self,request):
        pass

