class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        sum = 0
        if n == 1 or n==2:
            return 1
        else:
            for i in range(n):
                sum += i
                if sum < n:
                    continue
                elif sum == n:
                    return i
                else:
                    return i-1