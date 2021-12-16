class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)   #dp数组：动态规划 记录每一步得到的结果
                         #注意 n与n+1   在这里为了保证后面的dp[n],要建立n+1长度
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]
