#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-12
背包问题

动态规划
'''


# 找到最小重量单位
def find_min_weight(goods, total_weight):
    min_weight = total_weight+1
    for i in goods:
        g_weight = goods[i][0]
        if min_weight > g_weight:
            min_weight = g_weight
    if min_weight > total_weight:
        return None
    return min_weight


# 最佳选择
def optimal_choice(goods, total_weight):

    # 最小重量单位
    min_weight = find_min_weight(goods, total_weight)
    if min_weight is None:
        return None

    # 列数
    multiple = int(total_weight//min_weight)
    columns = multiple if total_weight % min_weight == 0 else multiple + 1
    # 构建网格，网格的最小单位为list ［［物品集］，列容量，最优价值］
    cell = [[[[], (c+1) * min_weight, 0] for c in range(columns)]
            for r in range(len(goods))]

    row = 0
    # 逐行填充物品集和最优价值
    for g, p in goods.items():
        grow = cell[row]
        # 第零行直接填充
        if row == 0:
            for gcol in grow:
                if gcol[1] >= p[0]:
                    # goods类型，价值
                    gcol[0].append(g)
                    gcol[2] = p[1]
        # 其他行 比同列前行价值 与 （当前行物品价值 ＋ 剩余容量价值），取最大价值
        else:
            for col, gcol in enumerate(grow):
                # 新重量：当前行物品价值 ＋ 剩余容量价值
                mul= int((gcol[1]-p[0])//min_weight)
                residual_col = mul - 1
                new_weight = p[1] + cell[row -
                                         1][residual_col][2] if residual_col >= 0 else p[1]
                # 当前行物品重量不大于当前列容量，且新重量大于同列上行
                if gcol[1] >= p[0] and new_weight > cell[row-1][col][2]:
                    cell[row][col][2] = new_weight
                    cell[row][col][0] = cell[row-1][residual_col][0] + \
                        [g] if residual_col >= 0 else [g]
                # 当前行物品重量小于当前列容量 且 当前行物质价值
                else:
                    cell[row][col][2] = cell[row-1][col][2]
                    cell[row][col][0] = cell[row-1][col][0]
        row += 1

    return cell[-1][-1]


if __name__ == '__main__':
    goods = {}
    goods['吉他'] = (1, 1500)
    goods['音响'] = (4, 3000)
    goods['笔记本'] = (3, 2000)
    goods['项链'] = (0.5, 1000)

    total_weight = 4.5

    print(optimal_choice(goods, total_weight))
