class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res^i
        return res

# 0,1异或：相同为0，不同为1
'''
交换律：a ^ b ^ c <=> a ^ c ^ b

0 ^ x => x
n ^ n => 0 相同为0

var a = [2,3,2,4,4]
2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
'''
