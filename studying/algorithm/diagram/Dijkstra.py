#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-12
狄克斯特拉算法
找出带权图中的最短路径(不可以算负权边的图)


1. 先初始化从start 直接到达其他所有节点的距离，存入costs
2. 取costs中最短距离的节点，若经该节点到达后续节点的距离小于原costs中到达后续节点的距离，更新costs
3. 用parents 记录路径
'''


from collections import deque


# 初始化costs
def costs_init(graph, start):
    costs = {}
    for k in graph:
        if k != start:
            if k in graph[start]:
                costs[k] = graph[start][k]
            else:
                costs[k] = float('inf')
    return costs


# 初始化parents
def parents_init(graph, start):
    parents = {}
    for k in graph:
        if k != start:
            if k in graph[start]:
                parents[k] = start
            else:
                parents[k] = None
    return parents


# 查找最短路径
def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 狄克斯特拉算法
def dijkstra_search(graph,  start, end):

    result = deque()
    processed = []
    costs = costs_init(graph, start)
    parents = parents_init(graph, start)

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for nnode, ncost in neighbors.items():
            new_cost = cost + ncost
            if costs[nnode] > new_cost:
                costs[nnode] = new_cost
                parents[nnode] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    result.append(end)
    node = end
    while node and node != start:
        node = parents[node]
        result.appendleft(node)

    if node == start:
        return (costs[end], result)
    else:
        return None


if __name__ == '__main__':
    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2

    graph['a'] = {}
    graph['a']['fin'] = 1
    # graph['a']['start'] = 1

    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5

    graph['fin'] = {}

    # infinity = float('inf')
    # costs = {}
    # costs['a'] = 6
    # costs['b'] = 2
    # costs['fin'] = infinity

    # parents = {}
    # parents['a'] = 'start'
    # parents['b'] = 'start'
    # parents['fin'] = None

    cost, path = dijkstra_search(graph, 'start', 'fin')
    print('距离：%s' % cost, '路径：', '->'.join(path))
