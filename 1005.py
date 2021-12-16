class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        B=sorted(nums)
        for i in range(k):
            B[0]=-B[0]
            B=sorted(B)
        return sum(B)