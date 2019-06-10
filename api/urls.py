#encoding:utf-8
from django.urls import path,include
from api.Account.views import UserLoginView

urlpatterns = [
    path('account/', include([
        path("login",UserLoginView.as_view(),name='login')
    ])),
]