class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_5=0
        while n > 0:
            count_5 = count_5 + n//5
            n = n//5
        return count_5

        #return n // 5 + n // 25 + n // 125 + n // 625 + n // 3125 + n // 15625 + n // 78125 + n // 390625 + n // 1953125 + n // 9765625 + n // 48828125 + n // 244140625 + n // 1220703125

    
