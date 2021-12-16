class Solution:
    def originalDigits(self, s: str) -> str:
        n0 = s.count('z')
        n2 = s.count('w')
        n8 = s.count('g')
        n6 = s.count('x')
        n3 = s.count('t') - n2 - n8
        n4 = s.count('u')
        n7 = s.count('s') - n6
        n1 = s.count('o') - n4 - n2 - n0
        n5 = s.count('v') - n7
        n9 = s.count('i') - n8 - n6 - n5

        n = (n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)

        return "".join((str(i)*j for i, j in enumerate(n)))#enumerate输出序列号i和被遍历的元组（i_0,n_0)(i_1,n_1)