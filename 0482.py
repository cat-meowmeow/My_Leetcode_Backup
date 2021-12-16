class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s_ = S.replace('-','')
        n = len(s_)
        first = n%K
        res = ''
        for i in range(0,first):
            res = res+s_[i]
        for j in range(first,n):
            if (j-first)%K==0 and res!='':
                res = res+'-'+s_[j]
            else:
                res = res+s_[j]
        return res.upper()
