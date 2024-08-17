# 删除链表中倒数第n 个节点。思路对50%，但是实现方式未想到（快慢指针方式）
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 记录前驱节点、当前节点、后继节点
        # 当前节点之后第n-1个是否是末节点
        # 是，前驱节点next 指向后继节点
        # 哑结点指向head
        # 适用快慢指针实现，两个指针间间隔n
        # 当快指针下一个节点是末节点时，删除慢指针的下一个节点
        pre = ListNode(None)
        pre.next = head
        start,end = pre ,pre
        while n != 0 :
            start = start.next
            n -= 1
        while start.next != None :
            start = start.next
            end = end.next
        end.next = end.next.next
        return pre.next
