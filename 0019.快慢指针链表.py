class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n ==1 and head.next == None: #排除只有一个数字特例
            return print('[]')
        slownode = ListNode(None)
        fastnode = ListNode(None)
        slownode.next = head        #起始节点，指向该链表head
        fastnode.next = head

        for i in range(n):              #快指针先走n格
            fastnode = fastnode.next
        while (fastnode.next != None):      #当快指针存在时
            slownode = slownode.next        #快慢一起走向下一位
            fastnode = fastnode.next

        if slownode.next == head:           #特殊情况：如果头指针相等
            head = head.next                #删除头节点（头节点改为下一个
        else:
            slownode.next = slownode.next.next  #慢指针跳过该节点
        return head         #返回的是该链表而非slownode链表

#Leetcode 19
