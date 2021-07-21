# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/21 16:12

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        exists_dict = {}
        tmp = headA
        while tmp:
            exists_dict[tmp] = 1
            tmp = tmp.next
        tmp = headB
        while tmp:
            if exists_dict.get(tmp):
                return tmp
            tmp = tmp.next
        return None

if __name__ == "__main__":
    test = Solution()

