class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1] * n  # 定义数组
        count = 0
        for i in range(2, n):          # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                for j in range(i*i, n, i):  # 从i*i开始更快，每隔i标记一次
                    is_prime[j] = 0

        return count
