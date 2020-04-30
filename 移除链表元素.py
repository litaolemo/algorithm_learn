# -*- coding:utf-8 -*-
# @Time : 2020/4/30 17:23 
# @Author : litao
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        l = ans
        r = ans.next
        while r:
            if r.val == val:
                l.next = r.next

            else:
                l = l.next
            r = r.next
        return ans.next


a = [1,2,6,3,4,5,6]
ars = ListNode(0)
for count,i in enumerate(a):
    ars.val = i
    ars.next = a