#!/usr/bin/env python
from django.conf.urls import url
from ajax01.views import *
urlpatterns = [
    url(r'^index/',index),
    url(r'^demo/', demo), #timer(request)
    url(r'^ajax_send/',ajax_send,name='ajax'),
    url(r'^user/valid/',user_valid,name='user_valid'),
    url(r'^login/',login,name='login'),
]