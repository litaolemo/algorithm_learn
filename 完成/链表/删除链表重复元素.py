# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 20:47
# @Author  : litao


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        # write code here
        exists_dict = {}
        tmp = head
        last_link = head
        next_link = None
        try:
            while isinstance(head.val,int):
                if head.val in exists_dict:
                    last_link.next = head.next
                    head = head.next
                    continue
                else:
                    last_link = head
                    exists_dict[head.val] = 1
                    head = head.next
        except:
            pass
        return tmp

lis = [-50,-50,-49,-49,-49,-47,-46,-46,-46,-42,-41,-41,-40,-40,-39,-39,-38,-38,-38,-37,-36,-36,-36,-36,-35,-35,-34,-34,-33,-31,-31,-31,-30,-29,-27,-27,-26,-26,-22,-22,-21,-21,-21,-19,-18,-18,-18,-18,-18,-18,-17,-16,-15,-14,-14,-14,-13,-13,-11,-10,-10,-9,-9,-8,-8,-7,-6,-5,-5,-3,-1,0,0,0,1,1,4,5,6,6,6,6,7,9,10,10,11,12,13,14,15,15,15,16,16,16,16,19,20,24,26,28,28,30,31,34,34,36,38,39,39,40,41,42,42,44,44,45,48,49,49,50,50,50]
listnode = ListNode(lis[0])
temp = listnode
for count,l in enumerate(lis):
    if count >= 1:
        temp_node = ListNode(l)
        temp.next = temp_node
        temp = temp.next

# res.deleteNode(a,1)
test = Solution()
test.deleteDuplicates(listnode)
print(listnode.val)
while listnode.next:
    listnode = listnode.next
    print(listnode.val)
