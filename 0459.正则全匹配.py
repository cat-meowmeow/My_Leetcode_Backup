class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        import re
        r1 = re.compile(r'([a-z]+)\1+')
        if re.fullmatch(r1,s):
            return True
        else:
            return False
