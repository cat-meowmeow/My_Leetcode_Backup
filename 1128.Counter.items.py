class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        a = []
        for i, j in dominoes:
            a.append(str(sorted([i,j])))
        ans = 0
        for k, v in dict(collections.Counter(a)).items():
            if v > 1:
                ans += v*(v-1)//2
        return ans
'''
c.items()  # 转为(elem, cnt)格式的列表
'''

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic={}
        res=0
        for num in dominoes:
            num.sort()
            c=(num[0],num[1])
            if  c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        for v in dic.values():
            if v >1:
                res+=v*(v-1)//2
        return res
