class Solution:
    def toHex(self, num: int) -> str:
        return hex(num&0xFFFFFFFF)[2:]#负数转无符号的十六进制数，看不懂反正就是位运算和补码
