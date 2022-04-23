from django.urls import path

from .views import *

urlpatterns = [
    path('register', register),  # 指定register函数的路由为register
    path('login', login),
    path('logout', logout),
    path('release', release),
    path('search_list', search_list)
]
