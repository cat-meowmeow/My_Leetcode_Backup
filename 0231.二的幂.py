class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:return False
        #直接位运算：判断2的幂 return ( n&(-n)==n )
        while n != 1:
            if n%2 == 0:
                n = n//2
            else:
                return False
        return True
