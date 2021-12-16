class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  #存放符合条件结果的集合
        path = []  #用来存放符合条件的结果
        used = []  #用来存放已经用过的数字
        def backtrack(nums,used):
            if len(path) == len(nums):
                return res.append(path[:])  #此时说明找到了一组
                
            for i in range(0,len(nums)):
                if nums[i] in used:
                    continue  #used里已经收录的元素，直接跳过
                path.append(nums[i])
                used.append(nums[i])
                
                backtrack(nums,used)
                
                used.pop()
                path.pop()
        
        backtrack(nums,used)
        return res
        
'''
result = []
def backtrack(路径, 已选择的列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:]
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res
 
 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         res = []
        def backtrack(nums,one_permute):
            if not nums:
                res.append(one_permute)
                return
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
            backtrack(nums,[])
            return res
