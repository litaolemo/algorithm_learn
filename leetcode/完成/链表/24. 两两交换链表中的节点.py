# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/21 13:43


"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next

    class Solution:
        def swapPairs(self, head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            newHead = head.next
            head.next = self.swapPairs(newHead.next)
            newHead.next = head
            return newHead


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    test = Solution()
    res = test.swapPairs(l1)
    while res.next:
        print(res.val)
        res = res.next