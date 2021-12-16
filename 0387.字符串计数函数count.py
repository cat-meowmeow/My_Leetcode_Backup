class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j and s[j] == s[i]:
                    break
            else:
                return i
        return -1
