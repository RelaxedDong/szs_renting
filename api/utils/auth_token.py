#encoding:utf-8

import jwt
import base64
import time,json

print(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(1560273022)))
# def verify_bearer_token():
#     result  = base64.b64decode("eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IiIsImV4cCI6MTU2MDI3MzAyMiwiZW1haWwiOiIifQ==".encode('utf-8'))
#     print(type(result))
#     otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
#     print
#     otherStyleTime
#     return result

result = jwt.decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IiIsImV4cCI6MTU2MDM0OTExOCwiZW1haWwiOiIifQ.JepB3lRbzrA7jcNyTchmXC1GAUv-os1OIua1WRaeaHU",algorithms=['HS256'])
print(result)
# verify_bearer_token()