#! /usr/bin/env python3
# -*- coding:utf8 -*-


'''
 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将第一天剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，发现只剩下一个桃子了。编写程序求猴子第一天共摘了多少个桃子。 
'''


def compute():
    number = 1
    for day in range(9):
        number = (1+number)*2
    print('桃子的数量为：%s' % number)


if __name__ == '__main__':
    compute()
