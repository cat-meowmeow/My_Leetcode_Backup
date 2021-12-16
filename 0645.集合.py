class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        n = len(nums)
        s = [0]*n
        for i in range(n):
            s[i] = i+1
        sum_s = sum(s)
        sum_num = sum(nums)
        c = sum_s-sum_num
        set_s = set(s)
        a = set_s - set_nums
        b = a.pop()            #还好集合只有一个元素，直接pop出来
        d = b-c
        return [d,b]



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))  #集合可以直接加法
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]
