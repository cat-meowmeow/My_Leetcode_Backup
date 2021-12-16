class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1 == 1:      # odd
            return 'a'*n
        if n & 1 == 0:      # even
            return 'a'*(n-1)+'b'
