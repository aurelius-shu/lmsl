# -*-coding:utf-8 -*-
def shellSort(input_list):
	length = len(input_list)
	if length <= 1:
		return input_list
	sorted_list = input_list
	gap = length // 2
	while gap > 0:
		for i in range(gap, length):
			j = i - gap
			temp = sorted_list[i]
			while j >= 0 and temp < sorted_list[j]:
				sorted_list[j+gap] = sorted_list[j]
				j -= gap
			sorted_list[j+gap] = temp
		gap //= 2
	return sorted_list 

if __name__ == '__main__':
	input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
	print('排序前:', input_list)
	sorted_list = shellSort(input_list)
	print('排序后:', sorted_list)