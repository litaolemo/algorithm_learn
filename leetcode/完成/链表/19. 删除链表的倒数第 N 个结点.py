# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/20 14:53

"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target_node = head
        head_node = head
        count = 0
        while head.next:
            count += 1
            if count > n-1:
                tempnode = target_node
                target_node = target_node.next
            head = head.next
        try:
            tempnode.next = target_node.next
        except:
            return head_node.next
        return head_node

if __name__ == "__main__":
    test = Solution()
