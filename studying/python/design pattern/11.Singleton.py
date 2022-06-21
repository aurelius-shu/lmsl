#!/usr/bin/env python3
#-*- coding: utf-8 -*-


'''
单例模式
使用模块，Python的模块是天然的单例，模块第一次导入时，会生成.pyc文件，第二次导入时，会直接加载.pyc文件
'''

class Singleton(object):
    def foo(self):
        pass

singleton = Singleton()


