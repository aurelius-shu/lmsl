#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
66. 矩阵中的路径

'''


# 矩阵中是否存在path的路径
def has_path(matrix, path):
    if not matrix or not matrix[0] or not path:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [False for i in range(rows*cols)]
    pathLength = 0
    # 挨个遍历
    for row in range(rows):
        for col in range(cols):
            # 判断从此处进入是否可以走通
            if has_path_core(matrix, row, col, path, pathLength, visited):
                return True

    del visited
    return False


# 判断从此处进入是否可以走通
def has_path_core(matrix, row, col, path, pathLength, visited):
    # 走通了path
    if pathLength == len(path):
        return True

    haspath = False
    rows = len(matrix)
    cols = len(matrix[0])
    # 当前点在matrix中，正是path的一下步，且没有被visited过，则该节点匹配成功
    if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row][col] == path[pathLength] and not visited[row*cols+col]:
        pathLength += 1
        visited[row*cols+col] = True
        # 从当前结点的上下左右寻找下一个结点
        haspath = has_path_core(matrix, row-1, col, path, pathLength, visited) or has_path_core(matrix, row+1, col, path, pathLength, visited) or has_path_core(matrix, row, col-1, path, pathLength, visited) or has_path_core(matrix, row, col+1, path, pathLength, visited)
        # 若没有一下结点，path退一步
        if not haspath:
            pathLength -= 1
            visited[row*cols+col] = False
    return haspath


if __name__ == '__main__':
    matrix = [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]
    print(has_path(matrix, 'bcced'))
