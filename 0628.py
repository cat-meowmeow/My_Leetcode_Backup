class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:return nums[0]*nums[1]*nums[2]
        a = max(nums)
        b = min(nums)
        nums.remove(a)
        aa = max(nums)
        nums.remove(aa)
        aaa = max(nums)

        nums.remove(b)
        bb = min(nums)
        return max(a*aa*aaa,a*b*bb)
