class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:return False
        x = [1,2,3,5]
        while num not in x:
            if num %2 == 0:
                num = num//2
            elif num % 3 == 0:
                num = num//3
            elif num % 5 ==0:
                num = num//5
            else:
                return False
        return True
