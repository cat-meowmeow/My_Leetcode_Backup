class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        cur = head #直接修改原head链表，所以新建cur指针

        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next#跳过该值
            else:
                cur = cur.next#不跳过，正常指针移动一步
        return head