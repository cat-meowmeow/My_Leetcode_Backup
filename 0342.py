class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:return False
        while n %4 ==0:
            n = n/4
        return n==1



from math import log2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
