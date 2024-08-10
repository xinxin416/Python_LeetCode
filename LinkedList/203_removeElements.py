
##Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        '''
        ## 链表本身递归特征。当头结点等于目标值，头结点需要被删除，删除后的头结点是heda.next
        ## 如果头结点不等于目标值，保留头结点，删除操作后的头结点仍然是head
        if head == None :
            return None
        head.next = self.removeElements(head.next,val )
        if head.val == val :
            return head.next
        else :
            return head
        '''
        ## 迭代。用temp表示当前节点。如果temp.next 不为空且等于目标值，删除temp下一个节点， temp.next = temp.next.next
        # 如果temp.next 不等于目标值，保留下一个节点， temp 移动到下一个节点
        # 由于头结点可能会被删除，创建哑节点
        dummyHead = ListNode # 哑节点
        dummyHead.next = head
        temp = dummyHead # 当前节点
        while temp.next != None :
            if temp.next.val == val :
                temp.next = temp.next.next
            else :
                temp = temp.next
        return dummyHead.next