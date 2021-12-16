class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i,n):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i],nums[j]=nums[j],nums[i]

# 优化:
        n = len(nums)
        i=j=0
        while j < n :
            if nums[j] != 0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
