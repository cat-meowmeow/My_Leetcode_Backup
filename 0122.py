class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profits = 0
        for i in range(1, n):
            if (prices[i]-prices[i-1])>0:
                profits = (prices[i]-prices[i-1]) + profits
        return profits
