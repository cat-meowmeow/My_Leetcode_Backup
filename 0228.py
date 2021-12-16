class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = 0
        end = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i+1] - nums[i] == 1:
                end += 1
            else:
                if start != end:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                else:
                    res.append(str(nums[start]))

                if i + 1 < len(nums) and nums[i+1] - nums[i] != 1:
                    start = i + 1
                    end = i + 1
        return res
