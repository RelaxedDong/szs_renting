#encoding:utf-8
from django.urls import path,include
from api.account.views import UserLoginView
from api.house.views import index

urlpatterns = [
    path('account/', include([
        path("login",UserLoginView.as_view(),name='login'),
    ])),
    path('house/',include([
        path("index",index,name='index'),
    ]))
]