class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code *3
        s = []

        if k <0:
            for i in range(n,n*2):
                s.append(sum(code[i+k:i]))
        elif k>0:
            for i in range(n,n*2):
                s.append(sum(code[i+1:i+1+k]))
        elif k==0:
            s = [0]*n
        return s
