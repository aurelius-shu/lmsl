#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
单例模式
基于MetaClass实现（引入线程安全）
'''


import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            with SingletonType._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super().__call__(*args, **kw)

        return cls._instance


class Singleton(metaclass=SingletonType):
    def __init__(self, name):
        self._name = name

    def printname(self):
        print(self._name)


if __name__ == '__main__':
    # print('aaa'),
    # print('bbb')
    singleton = Singleton('aaa')
    singleton.printname()
    singleton = Singleton('bbb')
    singleton.printname()
