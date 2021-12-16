class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        n = len(score)
        num = 0
        place = 0
        a = score[:]
        a.sort(reverse = True)

        while num < n:# in score
            while place < n:# in a
                if score[num] == a[place]:
                    res.append(place+1)
                    place = 0
                    num = num+1
                    break
                else:
                    place += 1
        
        for i in range(n):

            if res[i] == 1:
                res[i] = "Gold Medal"
            elif res[i] == 2:
                res[i] = "Silver Medal"
            elif res[i] == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(res[i])
        return res