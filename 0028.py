class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        for i in range(0,m-n+1):    #切片
            if haystack[i:i+n]==needle:
                return i
        return -1   #没有返回的就返回-1
