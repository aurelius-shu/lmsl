#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
单例模式
类方法实现（引入线程安全）
'''


import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kw):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton(*args, **kw)
        return Singleton._instance
