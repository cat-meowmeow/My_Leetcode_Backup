class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofits = 0

        for i in range(0,n-1):
            for j in range(i+1,n):
                minus = prices[j]-prices[i]
                if maxprofits < minus:
                    maxprofits = minus
        return maxprofits


class Solution:   #一次遍历
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        profit = 0

        for price in prices:
            profit = max(price - minprice, profit)  #计算利润，并更新最大利润
            minprice = min(price, minprice)         #更改最小值
        return profit
