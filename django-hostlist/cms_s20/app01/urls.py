#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
from django.conf.urls import url
from app01.views import *
urlpatterns = [
    url(r'^timer/', timer), #timer(request)
    url(r'^book/(\d+)$', book_detail), #book_detail(request,\d+)
    url(r'^book_achrive/(\d+)/(\d+)$', book_achrive),  # book_detail(request,\d+,\d+)
    url(r'^book_achrive/(?P<year>\d+)/(?P<month>\d+)$', book_achrive),  # book_detail(request,year=\d+,month=\d+) #有名分组
]

#url 的路径与正则匹配
#分组：(\d+)
