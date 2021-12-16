import numpy as np
from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        arr = []
        for (x0,y0),(x1,y1),(x2,y2) in combinations(points,3):
            arr.append(abs(np.linalg.det(np.array([[x0,y0,1],[x1,y1,1],[x2,y2,1]]))))
        return max(arr)/2
'''
np.linalg.det  行列式求值
combinations(points,3) 求点坐标组合
'''
