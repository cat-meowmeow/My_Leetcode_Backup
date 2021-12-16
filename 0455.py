class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        n =len(g)
        for i in s:
            if i >= g[j]:
                j += 1
            if j == n:break
        return j
