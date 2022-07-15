# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def deleteNode(head, val):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if head.val == val:
            return head.next
        temp = head
        while temp.next:
            # print(temp.next.val)
            if temp.next.val == val:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head


if __name__ == "__main__":
    lis = [-3,5,-99]
    val = -99
    listnode = ListNode(lis[0])
    temp = listnode
    for count,l in enumerate(lis):
        if count >= 1:
            temp_node = ListNode(l)
            temp.next = temp_node
            temp = temp.next

    # res.deleteNode(a,1)
    test = Solution()
    test.deleteNode(listnode,val)
    print(listnode.val)
    while listnode.next:
        listnode = listnode.next
        print(listnode.val)
