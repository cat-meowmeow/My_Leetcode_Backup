# 暴力法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l = []    #用元组更好 l = set()
        cur1 = headA                  #从 头开始
        cur2 = headB
        while cur1:                   #先把listNode A写入数组l
            l.append(cur1)  #l.add(cur1)
            cur1 = cur1.next
        while cur2:                    #cur2 从头开始，一个一个与l进行比对
            if cur2 in l:
                return cur2
            else:
                cur2 = cur2.next
        return

#拼接链表  双指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:return None

        nodeA = headA
        nodeB = headB
        while (nodeA != nodeB):         #有交点就会相遇，返回节点nodeA
            if nodeA:                   #无交点相当于在null处相遇
                nodeA = nodeA.next
            else:
                nodeA = headB           #A到末尾null时候，转到B链表头结点
            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA
        return nodeB
