#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-15
13. 在O(1)时间删除链表结点

测试用例：
功能测试：输入链表有一个或多个结点，被删除结点在链表的尾部或非尾部
特殊输入测试：链表为空
'''


def delete_node(List, startPointer, toBeDeleted):
    if List == None or toBeDeleted == None:
        return None

    # 要删除的结点不是尾结点，与下个结点交换，删除下个结点
    if List[toBeDeleted]['pointer'] != None:
        nextNode = List[List[toBeDeleted]['pointer']]
        List[toBeDeleted]['pointer'] = nextNode['pointer']
        List[toBeDeleted]['value'] = nextNode['value']
    # 链表只有一个结点，删除头结点
    elif len(List) == 1:
        List = {}
    # 链表有多个结点，遍历找到上一个界点，删掉尾结点
    else:
        curNode = List[startPointer]
        while List[curNode['pointer']]['pointer'] != None:
            curNode = List[curNode['pointer']]
        curNode['pointer'] = None

    if List == None or List == {}:
        print('链表为空')
        return
    curNode = startPointer
    while List[curNode]['pointer'] != None:
        print(curNode, List[curNode]['value'])
        curNode = List[curNode]['pointer']
    print(curNode, List[curNode]['value'])


if __name__ == '__main__':
    List = {}
    # List['a'] = {'pointer': 'b', 'value': 'va'}
    # List['b'] = {'pointer': 'c', 'value': 'vb'}
    # List['c'] = {'pointer': 'd', 'value': 'vc'}
    List['d'] = {'pointer': None, 'value': 'vd'}

    delete_node(List, 'd', 'd')
