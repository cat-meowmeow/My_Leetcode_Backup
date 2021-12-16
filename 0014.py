class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        n = len(strs)
        for word in zip(*strs):
            if len(set(word)) == 1:
                res += word[0]
            else:
                break
        return res