class Solution:
    def climbStairs(self, n: int) -> int:
        x1 = 1
        x2 = 2
        if n<4:return n

        for i in range(3,n+1):  #循环法：（正向，也是从小到大算）
            x3 = x1 + x2        #   x1 + x2 ->  x3
            x1 = x2             #         |      |      |
            x2 = x3             #修改为   x1     x2     x3
        return x3



class Solution:
    def climbStairs(self, n: int) -> int:    #动态规划
        if n<4:return n
        dp = [0 for _ in range(n+1)]#dp=[0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):               #循环（缓存并复用结果）
            dp[i] = dp[i-1]+dp[i-2]          #写出递推公式（状态转移方程）
        return dp[n]                         #从小到大计算



#递归从后往前倒推
