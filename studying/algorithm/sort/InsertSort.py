# -*- coding:utf-8 -*-

def insertSort(input_list):
	if len(input_list) == 0:
		return []
	sorted_list = input_list

	for i in range(1, len(sorted_list)):
		temp = sorted_list[i]
		j = i - 1
		while j >=0 and temp < sorted_list[j]:
			sorted_list[j + 1] = sorted_list[j]
			j -= 1
		sorted_list[j + 1] = temp
	return sorted_list

if __name__ == '__main__':
	input_list = [6, 4, 8, 9, 2, 3, 1]
	print('排序前:', input_list)
	sorted_list = insertSort(input_list)
	print('排序后:', sorted_list)