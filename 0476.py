class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        y = ''
        for i in range(len(x)):
            y+=(str(1-int(x[i])))
        return int(y,2)
