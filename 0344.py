class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]   # 原地址拷贝，需要 切片=切片
        s.reverse()   # 自带
