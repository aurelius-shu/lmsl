#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
单例模式
基于__new__方法实现（引入线程安全）
'''

import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kw):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance
