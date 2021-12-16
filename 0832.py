class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = range(len(A))
        for i in n:
            A[i][:]=A[i][::-1]
        for row in n:
            for j in n:
                A[row][j]=A[row][j]^1
        return A

# return [[j^1 for j in row[::-1]] for row in A]
