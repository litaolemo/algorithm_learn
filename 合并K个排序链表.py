# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        stack = []
        for singleNode in lists:
            while singleNode:
                stack.append(singleNode.val)
                singleNode = singleNode.next
        resNode = tem = ListNode(0)
        stack.sort()
        for a in stack:
            tem.next = ListNode(a)
            tem = tem.next
        return resNode.next
