class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        words = S.split()
        res = []
        i = 1

        for word in words:
            if word[0] in vowel:
                w = word + 'ma' + 'a'*i
                i += 1
            else:
                w = word[1:]+word[0]+'ma'+'a'*i
                i+=1
            res.append(w)
        return ' '.join(res)
