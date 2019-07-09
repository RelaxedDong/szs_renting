# encoding:utf-8
from django.urls import path, include, re_path
from api.account.views import UserLoginView
from api.house.views import index, SearchListView, SelectItems, HouseDetailView

urlpatterns = [
    path('account/', include([
        path("login", UserLoginView.as_view(), name='login'),
    ])),
    path('house/', include([
        path("index", index, name='index'),
        path("search", SearchListView.as_view(), name='search'),
        path("selects", SelectItems.as_view(), name='selects'),
        re_path("^detail/(\d+)", HouseDetailView.as_view(), name='detail'),
    ]))
]
