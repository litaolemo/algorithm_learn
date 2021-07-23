# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/22 10:59

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.cachedNode = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        if not self.cachedNode.get(head):
            headnew = Node(head.val)
            self.cachedNode[head] = headnew
            headnew.next = self.copyRandomList(head.next)
            headnew.random = self.copyRandomList(head.random)
        return self.cachedNode.get(head)




if __name__ == "__main__":
    test = Solution()
    print(test.copyRandomList())