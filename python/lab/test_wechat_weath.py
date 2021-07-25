#! /usr/bin/env python3
# -*- coding:utf8 -*-


import requests
from bs4 import BeautifulSoup

import itchat
import datetime
import os
import platform
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


# 获取一个城市的天气信息
def get_weath(city_code):
    try:
        url = f'http://www.weather.com.cn/weather/{city_code}.shtml'
        resp = requests.get(url, headers=headers)
    except BaseException as e:
        print(e)
        return {}

    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 第一个包含 class = 'tem' 的 p 标签即为存放今天天气数据的标签
    tagToday = soup.find('p', class_='tem')
    try:
        # 最高温度
        temperatureHigh = tagToday.span.string
    except AttributeError:
        # 获取第二天的最高温度代替
        temperatureHigh = tagToday.find_next('p', class_='tem').span.string

    # 最低温度
    temperatureLow = tagToday.i.string
    # 天气
    weather = soup.find('p', class_='wea').string
    # 风力
    wind = soup.find('p', class_='win')
    # 穿衣指数
    clothes = soup.find('li', class_='li3 hot')

    return {'气温': f'{temperatureHigh}/{temperatureLow}', '天气': weather, '风力': wind.i.string, '穿衣': clothes.a.span.string + ','+clothes.a.p.string}


# dic 转字符串
def strDic(dic):
    str_weather = ''
    for key in dic:
        str_weather += key + ':'+dic[key]
        str_weather += '\n'
    return str_weather


def timerfun(sched_time):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now > sched_time and flag == 0:
            send_move('')
            flag = 1
            time.sleep(5)
        else:
            if flag == 1:
                sched_time = sched_time + datetime.timedelta(hours=1)
                flag = 0


def send_move(msg):
    # nickname = input('please input your firends\' nickname : ' )
    #   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    # users = itchat.search_friends(name=nickname)
    # friends = itchat.get_friends()
    # fds = []
    # for f in friends:
    #     fds.append(f['NickName'])
    users = itchat.search_friends(name=u'Zoe')   # 使用备注名来查找实际用户名
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    # 获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    itchat.send(msg + "\n该起来走动了！", toUserName=userName)
    print('succeed')


if __name__ == '__main__':
    # 深圳
    weath_bj = get_weath(101280601)
    itchat.auto_login(hotReload=True)
    print('Login Succeed')
    send_move(strDic(weath_bj))
    print('Send Move Succeed')