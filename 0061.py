# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k: return head
        n = 0
        head1 = head
        while head1:
            head1 = head1.next
            n+=1
        r = k % n  #r is final nodes 2
        s = n-r  # s is first nodes 1
        i = 0  # i is count
        cur = head     #不是cur = ListNode()
        res = cur
        head2 = head

        if r == 0:
            return head  
#直接res开始跳过前s项,不要动head原节点。(for即可)
        for i in range(s):
            res = res.next

        while cur.next:
            cur = cur.next
        cur.next = head2

        for j in range(s):
            cur = cur.next
        cur.next = None

        return res