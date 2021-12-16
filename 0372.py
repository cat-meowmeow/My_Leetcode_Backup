#超级次方
# a^b 对 1337 取模,b是数组[1,2]表示 ^12
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        r = 1
        a%=1337
        for i in b:
            r = pow(r,10)*pow(a,i)%1337
        return  r