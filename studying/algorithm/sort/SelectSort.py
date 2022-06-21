# -*- coding:utf-8 -*-

def SelectSort(input_list):
	'''
	函数说明:简单选择排序（升序）
	Author:
		www.cuijiahua.com
	Parameters:
		input_list - 待排序列表
	Returns:
		sorted_list - 升序排序好的列表
	'''	
	if len(input_list) == 0:
		return []
	sorted_list = input_list
	length = len(sorted_list)
	for i in range(length):
		min_index = i
		for j in range(i + 1, length):
			if sorted_list[min_index] > sorted_list[j]:
				min_index = j
		if min_index == i:
			break
		temp = sorted_list[i]
		sorted_list[i] = sorted_list[min_index]
		sorted_list[min_index] = temp
	return sorted_list

if __name__ == '__main__':
	input_list = [6, 4, 8, 9, 2, 3, 1]
	print('排序前:', input_list)
	sorted_list = SelectSort(input_list)
	print('排序后:', sorted_list)