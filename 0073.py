class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix) #rows
        n=len(matrix[0])#cols
        rows=set()
        cols=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            matrix[i]=[0]*n
        
        for j in cols:
            for k in range(m):
                matrix[k][j]=0