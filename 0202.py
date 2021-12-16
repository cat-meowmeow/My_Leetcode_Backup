class Solution:
    def isHappy(self, n: int) -> bool:
        sets = {1}
        sumi = n
        while sumi not in sets:
            sets.add(sumi)
            sumi = sum(int(i)**2 for i in str(sumi))
        return sumi == 1
