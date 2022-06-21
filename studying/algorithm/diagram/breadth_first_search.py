#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-12
广度优先搜索
'''


from collections import deque


def breadth_first_search(graph, start):
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('no mango seller!')
    return False


def person_is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['jonny'] = []

    breadth_first_search(graph, 'bob')
