# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 22:31
# @Author  : litao

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
def merge_ListNode(l1:ListNode,l2:ListNode):
    res = ListNode(None)
    node = res
    while l1 and l2:
        if l1.val < l2.val:
            node.next, l1 = l1, l1.next
        else:
            node.next, l2 = l2, l2.next
        node = node.next
    if l1:
        node.next = l1
    else:
        node.next = l2
    return res.next

if __name__ == "__main__":
    lis = [1,2,3]
    val = -99
    listnode = ListNode(lis[0])
    temp = listnode
    for count,l in enumerate(lis):
        if count >= 1:
            temp_node = ListNode(l)
            temp.next = temp_node
            temp = temp.next
    lis2 = [4,5,6]
    listnode1 = ListNode(lis2[0])
    temp1 = listnode1
    for count, l in enumerate(lis2):
        if count >= 1:
            temp_node = ListNode(l)
            temp1.next = temp_node
            temp1 = temp1.next
    res  = merge_ListNode(listnode,listnode1)
    pass