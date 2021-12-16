class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n =len(nums)
        for i in range(0,n):
            l_sum = 0
            r_sum = 0
            for a in range(0,i):
                l_sum += nums[a]
            for b in range(i+1,n):
                r_sum += nums[b]
            if l_sum==r_sum:
                return i 
        return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=sum(nums[:0])
        b=sum(nums[1:])
        for i in range(0,len(nums)-1):
            if a==b:
                return i
            a+=nums[i]
            b-=nums[i+1]
        if a==b:
            return len(nums)-1
        return -1
