#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/31 23:52


def create_user():
    pass

def create_superuser():
    pass

def run():
    user_type = input("create user type?(user or superuser)\n")
    if user_type == "user":
        pass

    elif user_type == "superuser":
        pass

    else:
        raise NameError("类型错误")


if __name__ == '__main__':
    run()