class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        nums = []
        s = s+'0'
        i = 0
        j = 0

        while i < n:
            j =i+1
            while j <n and s[i]==s[j]:
                j = j + 1
            if j-i>2:
                nums.append([i,j-1])
            i = j
        return nums
