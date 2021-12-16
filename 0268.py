class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_ = list(range(n+1))
        a = set(nums_)-set(nums)
        return a.pop()
