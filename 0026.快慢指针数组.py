'''
双指针
慢指针i   快指针j
起始位置i=0，j=1

慢指针不动，快指针+1，比较两值是否相等
    if 相等：
    慢的继续不动，快的+1
再次if比较——>（while语句

    if 不等：
    慢指针+1，将此快指针值赋给慢指针

当快指针直到数组末尾时结束，返回长度为 慢指针+1

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0


        i = 0
        j = 1

        while j != len(nums):
            if nums[i] == nums[j]:
                j = j+1
            
            else:
                i = i+1
                nums[i] = nums[j]
                j = j+1

        return i+1
