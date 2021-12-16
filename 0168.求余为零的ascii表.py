class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n > 0:
            n = n-1 # 需要减一 很重要  不减一的话n为26时right_num=0而非26
            right_num = n % 26
            right = chr(right_num+65)
            ans += right
            n = n//26
        
        return ans[::-1]
