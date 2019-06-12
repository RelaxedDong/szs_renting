import xadmin
from django.contrib.auth import get_user_model

class UserAdmin(object):
    list_display = ['username', 'email', 'date_joined', 'is_staff']
    search_fields = ['username', 'email', 'is_staff']
    list_filter = ['username', 'email', 'is_staff']


xadmin.site.unregister(get_user_model())
xadmin.site.register(get_user_model(),UserAdmin)