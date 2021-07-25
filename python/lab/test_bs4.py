#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aureliuls Shu'


'''
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup


def test_bs4():
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    bsObj = BeautifulSoup(html.read())
    print(bsObj.h1)


if __name__ == '__main__':
    test_bs4()
