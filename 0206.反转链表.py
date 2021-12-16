class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:                      
            forward = cur.next          # <-pre, cur-> , forward ->
            cur.next = pre              # <-pre, <-cur , forward ->
            pre,cur = cur,forward       # <-   , <-pre , cur|forward ->
        
        return pre