'''
i=0 j=0
如果不是数:
    nums[i] = nums[j]
    i++
    j++

如果是:
    慢指针原地不动，快指针+1前往下一个数
继续比较(循环
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i+1
                j = j+1
            
            else:
                j = j+1
        
        return i
