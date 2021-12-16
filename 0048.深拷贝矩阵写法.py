class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]    #新的深拷贝矩阵写法

        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]

        matrix[:] = matrix_new
