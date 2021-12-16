class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_ = list(set(nums))
        return (sum(nums)-sum(set_))//(len(nums)-len(set_))
