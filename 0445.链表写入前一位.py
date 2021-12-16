
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1=[]
        stack2=[]

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        ans = None

        while stack1 or stack2:
            num1 = 0 if not stack1 else stack1.pop()        #长度不够改为0
            num2 = 0 if not stack2 else stack2.pop()

            if num1+num2+carry>9:
                num3 = num1+num2+carry-10
                carry = 1
            else:
                num3 = num1+num2+carry
                carry = 0
            
            l3 = ListNode(num3)         #数字num3 写进链表，写入前一位
            l3.next = ans
            ans = l3                #输出的链表为ans
            
        if carry == 1:            #考虑头部进位情况,将1插在最前列
            a = ListNode(1)
            a.next = ans
            ans = a
        return ans



    
#leetcode 445
