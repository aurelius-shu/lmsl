#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
57. 删除链表中重复的结点

记录当前结点前的最晚访问过的不重复结点pPre、当前结点pCur、指向当前结点后面的结点pNext的三个指针
'''


from LinkList import ListNode


def delete_duplication(listHead):
    if not listHead:
        return None

    ppre, pcur, pnext = None, listHead, None
    while pcur:
        # 当前结点与下一个结点相同
        if pcur.next and pcur.value == pcur.next.value:
            pnext = pcur.next
            # 找到不重复的最后一个结点
            while pnext.next and pnext.next.value == pcur.value:
                pnext = pnext.next
            # 如果pcur是链表的第一个结点，即不存在ppre
            if pcur == listHead:
                listHead = pnext.next
            # 存在ppre
            else:
                ppre.next = pnext.next
            pcur = pnext.next
        # 当前结点与下一个结点不相同
        else:
            ppre = pcur
            pcur = pcur.next
    return listHead


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(6)
    listHead = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print(delete_duplication(listHead))
