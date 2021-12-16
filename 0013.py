class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0

        for i in range (len(s)):
            ans = ans+roman[s[i]]
        for j in range (len(s)-1):
            if roman[s[j]]<roman[s[j+1]]:
                ans = ans-2*roman[s[j]]
        return ans
