class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        i=0
        if x==0:
            return i

        while i < x:
            if i*i==x:
                return i
                break
            if i*i<x and x<(i+1)*(i+1):
                return i
                break
            else:
                i = i+1
