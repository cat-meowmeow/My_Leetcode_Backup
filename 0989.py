class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num_a = ''.join(list(map(str,A)))  # 数组拼接为整个数字：map变字符，join连接
        return list(map(int,str(int(num_a)+K))) #字符map int后拆分变回迭代列表
