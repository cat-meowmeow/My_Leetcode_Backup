class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<=1:return True
        if 0 not in nums[:n-1]:return True

        for i in range(n-2,-1,-1):   #倒序
            if nums[i]==0:
                for j in range(i-1,-1,-1):
                    if nums[j]>i-j:
                        break     #相当于这个0无效，停止j循环
                else:             #无法跨过这个0空隙
                    return False
        return True
