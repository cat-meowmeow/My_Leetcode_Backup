class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:return [-1,-1]
        import bisect
        n = len(nums)
        i = bisect.bisect_left(nums,target)
        if i< n and nums[i] == target:
            j = bisect.bisect_right(nums,target)-1
            return [i,j]
        else:
            return [-1,-1]
