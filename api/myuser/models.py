from django.db import models
from django.contrib.auth.models import UserManager,AbstractUser,AbstractBaseUser,PermissionsMixin
from django.utils import timezone

class User_Manager(UserManager):
    def _create_user(self, email,username, password, **extra_fields):
        if not email:
            raise ValueError("必须要传递email")
        if not password:
            raise ValueError("必须要传递密码")
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save()

    def create_user(self,email,username,password, **extra_fields):
        extra_fields['is_superuser'] = False
        return self._create_user(email,username,password,**extra_fields)

    def create_superuser(self,email,username,password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(email,username,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20,unique=True,verbose_name="用户名")
    email = models.EmailField(max_length=100,unique=True,verbose_name="邮箱")
    is_active = models.BooleanField(default=True,verbose_name="是否活跃")

    is_staff = models.BooleanField(
        default=True,
        verbose_name="员工"
    )

    date_joined = models.DateTimeField(verbose_name="加入时间",default=timezone.now)

    USERNAME_FIELD = 'email'
    FIRST_NAME_FIELD = 'username'

    objects = User_Manager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username




