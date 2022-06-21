#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
67. 机器人的运动范围

'''


def moving_count(threshold, rows, cols):
    count = 0
    # 如果位数和threshold 小于1 或者 方格不存在，直接返回0个格子
    if threshold < 1 or rows < 1 or cols < 1:
        return count

    # 用于存放已经走过的格子，避免重复累加
    visited = [False for i in range(rows*cols)]
    count = moving_count_core(threshold, rows, cols, 0, 0, visited)

    del visited
    return count


# 从该格子进入，还可以走多少格
def moving_count_core(threshold, rows, cols, row, col, visited):
    count = 0
    # 在格子范围内，且格子的位数和小于threshold，且该格子没有被访问过，则计算该格子，并求从其上下左右进入后，还可以走多少格
    if row >= 0 and row < rows and col >= 0 and col < cols and get_digit_sum(row)+get_digit_sum(col) <= threshold and not visited[row*cols+col]:
        visited[row*cols+col] = True
        count = 1 + moving_count_core(threshold, rows, cols, row+1, col, visited) + moving_count_core(threshold, rows, cols, row-1, col, visited) + \
            moving_count_core(threshold, rows, cols, row, col+1, visited) + \
            moving_count_core(threshold, rows, cols, row, col-1, visited)

    return count


# 求数值的位数和
def get_digit_sum(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum


if __name__ == '__main__':
    # (threshold, rows, cols)
    args = (10, 35, 37)
    print(args, args[1]*args[2])
    print(moving_count(*args))
