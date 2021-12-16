class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res,(j-i)*height[i])
                i += 1
            else:
                res = max(res,(j-i)*height[j])
                j -= 1
        return res
'''
双指针从两头开始
比较的是i与j的高度，而非他们之间面积
只有当后面一个的木板更长时才能i++,j--
'''
