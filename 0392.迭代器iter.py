class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:# 判断s是不是t的子序列
        t=iter(t)
        res=[]
        for ch in s:
            if ch in t:
                res.append(ch)
            else:
                res.append(0)
        return all(iter(res))
'''
        t = iter(t)
        return all(i in t for i in s)
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True。
'''
