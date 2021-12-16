class Solution:
    def fib(self, n: int) -> int:
        x1 = 0
        x2 = 1
        if n<2:return n

        for i in range(2,n+1):
            x3 = x1 + x2 
            x1 = x2
            x2 = x3 
        return x3



class Solution:
    def fib(self, N: int) -> int:
        a, b = 0,1
        for i in range(N):   #迭代
            a, b = b, a+b
        return a


# 递归
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
