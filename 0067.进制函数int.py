class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
'''
int()表示输入的a 为二进制形式
加法默认为十进制
bin返回  0b_ _  表明二进制数
[2:]舍去0b
'''
