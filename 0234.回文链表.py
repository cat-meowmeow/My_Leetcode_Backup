# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#简单用栈
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        n = 0
        stack = []
        cur = head

        while head:
            stack.append(head.val)
            head = head.next
            n = n+1
        
        n = n//2
        for i in range(n):
            pop = stack.pop()
            if pop == cur.val:
                cur = cur.next
            else:
                return False
        return True


#反转链表
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        def reverselist(cur):
            pre=None
            while cur:
                temp = cur.next
                cur.next = pre
                pre,cur = cur,temp
            return pre
        
        fast = head
        slow = head
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                break    

        part = reverselist(slow)#翻转的是slow剩下的部分

        while head.next:
            if head.val == part.val:
                head = head.next
                part = part.next
            else:
                return False
        return True