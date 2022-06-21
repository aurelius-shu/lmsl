# -*- coding:utf-8 -*-

def RadixSort(input_list):
	'''
	函数说明:基数排序（升序）
	Author:
		www.cuijiahua.com
	Parameters:
		input_list - 待排序列表
	Returns:
		sorted_list - 升序排序好的列表
	'''
	def MaxBit(input_list):
		'''
		函数说明:求出数组中最大数的位数的函数
		Author:
			www.cuijiahua.com
		Parameters:
			input_list - 待排序列表
		Returns:
			bits-num - 位数
		'''
		max_data = max(input_list)
		bits_num = 0
		while max_data:
			bits_num += 1
			max_data //= 10
		return bits_num

	def digit(num, d):
		'''
		函数说明:取数xxx上的第d位数字
		Author:
			www.cuijiahua.com
		Parameters:
			num - 待操作的数
			d - 第d位的数
		Returns:
			取数结果
		'''	
		p = 1
		while d > 1:
			d -= 1
			p *= 10
		return num // p % 10


	if len(input_list) == 0:
		return []
	sorted_list = input_list
	length = len(sorted_list)
	bucket = [0] * length
	
	for d in range(1, MaxBit(sorted_list) + 1):
		count = [0] * 10

		for i in range(0, length):
			count[digit(sorted_list[i], d)] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		for i in range(0, length)[::-1]:
			k = digit(sorted_list[i], d)
			bucket[count[k] - 1] = sorted_list[i]
			count[k] -= 1
		for i in range(0, length):
			sorted_list[i] = bucket[i]

	return sorted_list

if __name__ == '__main__':
	input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
	print('排序前:', input_list)
	sorted_list = RadixSort(input_list)
	print('排序后:', sorted_list)