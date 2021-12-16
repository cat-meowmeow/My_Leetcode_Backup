class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        set_A=set(A)
        res=[]

        if n != len(B):return False
        if A==B and len(set_A)<n:return True
        for i in range(n):
            if A[i]!=B[i]:
                res.append(A[i])
                res.append(B[i])
        if len(res)==4 and res==res[::-1]:return True
        else: return False
