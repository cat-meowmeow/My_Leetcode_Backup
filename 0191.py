class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)  #直接 return bin_n.count('1') 计算的是二进制bin下的位1数

        bin_str = str(bin_n)  #其实不需要转str
        n = bin_str.count('1')
        return n
