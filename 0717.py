class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count_1 = 0
        if len(bits)>2 and bits[-2] == 0:return True
        bits.pop()
        while bits:
            i = bits.pop()
            if i == 1:
                count_1 += 1
            else:
                break
        if count_1%2 == 0:
            return True
        else:
            return False
