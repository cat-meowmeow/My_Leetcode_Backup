class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        num = 0
        
        for i in A:      # 比如110100
            num = num*2+i   # 二进制转十进制   短除法，从下往上
            ans.append(num%5==0)
        return ans
