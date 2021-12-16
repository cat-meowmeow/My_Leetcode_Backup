class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = 0
        sum2 = 0

        for ch in s:
            sum1 = sum1 + ord(ch)
        for ch in t:
            sum2 = sum2 + ord(ch)
        return (chr(sum2-sum1))

'''
map一行代码：
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
'''
