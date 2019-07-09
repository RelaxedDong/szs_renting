import xadmin
from django.contrib.auth import get_user_model

class UserAdmin(object):
    list_display = ['username','email', 'is_active', 'last_login', 'is_staff','is_superuser']
    search_fields = ['username', 'is_active', 'is_staff']
    list_filter = ['username', 'email', 'is_active', 'is_staff']
    model_icon = 'fa fa-user-circle'

xadmin.site.unregister(get_user_model())
xadmin.site.register(get_user_model(),UserAdmin)