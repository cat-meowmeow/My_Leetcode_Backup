class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while (left<=right):
            mid = (right+left)//2
            if isBadVersion(mid) == True:
                right = mid-1
            else:
                left = mid +1
        return left
