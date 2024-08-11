'''
反转链表
方法一：通过双指针定义前驱节点、后继节点，在引用更改前存储前两个变量
方法二：递归
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 头结点作为尾节点，后一个节点的后继节点是前驱节点
        # 存储前一个节点，在更改引用前，存储后一个节点
        # 定义双指针
        pre = None
        cur = head
        while cur != None  :
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

