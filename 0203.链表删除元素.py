# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = ListNode()
        res = pre

        while head:
            if head.val == val:
                pre.next = head.next    #跳过语句： 继承语句，继承head.next地址，相当于pre链表里跳过该head.val
                head = head.next    # 前进语句
            else:
                pre.next = head      # 指向head节点                     ######
                pre = pre.next      #添加完元素后pre链表自己也要前进一位    ###### 两句联合是append语句
                head = head.next    # 前进语句
        return res.next