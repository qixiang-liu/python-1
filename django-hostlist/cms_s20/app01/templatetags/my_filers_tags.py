#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx

#自定义一个标签或者一个过滤器
from django import template
register=template.Library()

@register.filter
def multi_filter(x,y):

    return x * y


@register.simple_tag
def multi_tag(x, y):
    return x * y

