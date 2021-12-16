class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_ = n//2
        set_nums = set(nums)

        for i in set_nums:
            count_i = nums.count(i)
            if count_i>count_:
                return i
