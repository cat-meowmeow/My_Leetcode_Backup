class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_s = set(s)
        ans = 0
        j = 0
        for i in set_s:
            counti = s.count(i)
            if counti & 1 == 0:
                ans += counti
            else:
                ans += counti-1
                j = 1
        return ans+j
