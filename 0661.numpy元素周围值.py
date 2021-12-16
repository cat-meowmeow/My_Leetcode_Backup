class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        import numpy as np
        arr = np.array(M)
        gray_array = np.zeros(arr.shape)

        for row in range(arr.shape[0]):
            for col in  range(arr.shape[1]):
                gray_array[row,col] = np.average(arr[max(row-1,0):min(row+2,arr.shape[0]+1),max(col-1,0):min(col+2,arr.shape[1]+1)])
        gray_array=gray_array.astype(np.int)
        return gray_array


'''
一般情况     (row-1):(row+2)  注意算头不算尾，所以冒号后要多加1位
考虑左上角   max(row-1,0)
考虑右上角   min(row+2,shape['row']+1)
'''


# 取整
'''
类型type不变，数值value取整。
    截取整数部分 np.trunc
    向上取整 np.ceil
    向下取整np.floor
    四舍五入取整np.rint


类型type改变
    AA = np.array
    AA.astype(np.int)
'''
