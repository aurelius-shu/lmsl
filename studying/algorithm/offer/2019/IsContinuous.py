# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) < 5:
            return False
        numbers = sorted(numbers)

        count0 = 0
        for n in numbers:
            if n == 0: count0 += 1

        for i in range(count0, len(numbers) - 1):
            if numbers[i + 1] == numbers[i]:
                return False
            count0 -= numbers[i + 1] - numbers[i] - 1

        return count0 >= 0
