# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp = 0
        cur1 = l1
        cur2 = l2
        cur3 = ListNode()
        l3 = cur3 # 所以在cur3还没移动的时候注册l3，l3即从头算起（return cur3的头节点）

        while cur1 or cur2:
            if cur1:
                temp = temp + cur1.val
                cur1 = cur1.next #注意两句顺序
            if cur2:
                temp = temp + cur2.val
                cur2 = cur2.next
            
            num = temp%10
            temp = temp//10

            cur3.next = ListNode(num) #注意ListNode中的append语句格式，这里num是数字而非节点
            cur3 = cur3.next          ##注意ListNode中的append语句格式，这里num是数字而非节点  #两句联合是append语句
            
        if temp == 1:
            cur3.next = ListNode(temp)
# 这里  return cur3 就仅返回末节点,  return cur3.next 返回空节点
        return l3.next # return l3 的话，会有cur3的头节点，.next从下一位输出