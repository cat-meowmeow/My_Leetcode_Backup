class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        if n<=1:return True
        for i in range(1,n):
            if nums[i]< nums[i-1]:
                count+=1
            while count>1:
                return False   
            if i+1<n and i-1>0:
                if nums[i+1]< nums[i-1] and nums[i-2]>nums[i]:
                    return False 
        return  True
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        change = 1
        i = n-2
        while i > -1:
            if nums[i]>nums[i+1]:
                change -= 1
                nums[:]=nums[:i]
            if change <0:
                return False
            else:
                i -= 1
        return True
'''
