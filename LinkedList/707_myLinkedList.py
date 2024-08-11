'''
设计链表，定义一个类，管理链表的数据插入、删除以及元素获取方法
理解链表结构，val、next
该题中，定义链表size，在插入、删除操作时，注意更新链表长度
设置哨兵节点指向链表第一个元素
'''

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    ## 初始化，创建头结点和size
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


    def get(self, index):
        ## 返回下标为index 的节点值
        # 设置哨兵节点sentinel 作为头结点，依次遍历
        # 先判断下标有效性
        """
        :type index: int
        :rtype: int
        """
        if index <0 or index >=self.size :
            return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val


    def addAtHead(self, val):
        # 将val 插入到第一个元素之前，插入之后，新元素变成第一个元素
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size ,val )


    def addAtIndex(self, index, val):
        # 判断下标有效性
        # 遍历到索引index，找到其前驱节点，后继节点，创建新节点
        # 新节点next 指向后继节点，前驱节点 next 指向新节点（顺序不能反）
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return None
        index = max(0,index) # 如果在-1位置插入元素，即在头结点插入
        self.size += 1 # 链表长度+1
        pre = self.head
        for _ in range(index) :
            pre = pre.next

        to_add = ListNode(val)
        to_add.next = pre.next
        pre.next = to_add



    def deleteAtIndex(self, index):
        # 如果index 在尾部，前驱节点.next = None
        # 找到索引index 前驱节点、后继节点
        # 前驱节点.next = 前驱节点.next.next

        """
        :type index: int
        :rtype: None
        """
        if index <0 or index >= self.size:
            return None
        self.size -= 1 # 链表长度+1
        pre = self.head
        for _ in range(index) :
            pre = pre.next
        pre.next = pre.next.next



    # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)