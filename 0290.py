class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        s_list = s.split(' ')
        m = len(s_list)
        if n != m:return False

        for i in range(0,n-1):
            for j in range(1,n):
                if pattern[i] == pattern[j]:
                    if s_list[i] != s_list[j]:
                        return False
                else:
                    if s_list[i] == s_list[j]:
                        return False
        return True
