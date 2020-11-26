#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
单例模式
装饰器实现
'''


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]
    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self._x = x
