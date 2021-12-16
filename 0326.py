class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:return True
        if n < 0 :return False
        x = 1

        for i in range (0,20):
            x = 3*x
            if x == n:
                return True
            else:
                i += 1
        return False
