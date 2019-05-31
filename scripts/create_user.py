#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/31 23:52
from api.myuser.models import User

def create_user(email,username,password):
    User.objects.create_user(email=email, username=username, password=password)

def create_superuser(email,username,password):
    User.objects.create_superuser(email=email, username=username, password=password)


def run():
    user_type = input("create user type?(user or superuser)\n")
    if user_type not in ['user','superuser']:
        raise NameError("类型错误")

    if user_type == "user":
        email = input("email?\n")
        username = input("username?\n")
        password = input("password?\n")
        create_user(email,username,password)

    elif user_type == "superuser":
        email = input("email?\n")
        username = input("username?\n")
        password = input("password?\n")
        create_superuser(email,username,password)


