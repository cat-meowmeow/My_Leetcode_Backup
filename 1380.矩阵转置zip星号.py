class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin = set()
        colmax = set()

        for i in matrix:
            rowmin.add(min(i))
        for j in zip(*matrix):   #zip将多列压缩，zip(*）将矩阵解压为列
            colmax.add(max(j))
        
        return list(rowmin & colmax)
