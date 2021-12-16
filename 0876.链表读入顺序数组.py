class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nums = []    #链表数组只能从头读取

        while head:  #head值存放进第一个值
            nums.append(head) #读入数组
            head = head.next  #链表推进读取

        return nums[len(nums)//2]
