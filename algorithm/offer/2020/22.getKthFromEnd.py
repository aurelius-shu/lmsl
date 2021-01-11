#-*- coding:utf-8 -*-
"""
题目：
    22. 链表中倒数第k个节点
    输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
    
思路：
    双指针，一先一后，步数相差k

注意：
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if k < 0:
            raise ValueError('input error, k must be bigger than 0')

        first, later = head, head
        while first.next and k -1 >0:
            k-=1
            first = first.next

        if k - 1 > 0:
            raise ValueError('input error, k must be bigger than the length of head')

        while first.next:
            first = first.next
            later = later.next

        return later

s = Solution()
res = s.exchange([1, 2, 3, 4])
print(res)
