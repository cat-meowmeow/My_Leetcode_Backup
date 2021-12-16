class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s1 = s.lower()
        s2 = re.sub(r'[^0-9a-z]','',s1)
        re_s = s2[::-1]
        return s2 == re_s
