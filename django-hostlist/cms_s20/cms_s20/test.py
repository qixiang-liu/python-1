#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        # print(b)
        a = b
        b = a + b
        n = n + 1
        print('a=%s,b=%s,n=%s,max=%s'%(a,b,n,max))
    return a,b,n,max


def fibb(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        a, b = b, a + b
        n = n + 1
        print('a=%s,b=%s,n=%s,max=%s' % (a, b, n, max))
    return a,b,n,max
fib(10)
fibb(10)