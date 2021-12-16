class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        temp = set(deck)
        count = []
        i=0

        for num in temp:
            for nums in deck:
                if nums == num:
                    i += 1
            count.append(i)
            i = 0
        # 以上count可以直接调包 count = collections.Counter(deck) 用于计算[]中每个数字出现次数
        
        
        N = len(deck)
        for X in range(2, N + 1):
            if N % X == 0:
                if all(v % X == 0 for v in count):
                    return True
        return False



class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N + 1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False
