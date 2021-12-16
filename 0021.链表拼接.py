class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0) #多申请一个带输出链表头结点
        last = head; # 该带输出链表末节点   链表添加元素只对尾节点操作，返回时输出头结点指针即可

        while l1 and l2:
            if l1.val <= l2.val:
                last.next = l1 # 新链表记录下l1
                l1 = l1.next
            else: 
                last.next = l2
                l2 = l2.next
            last = last.next
        if l1:
            last.next = l1
        elif l2:
            last.next = l2
        return head.next

##############

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

