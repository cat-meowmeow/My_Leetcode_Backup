class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        licensePlate = Counter(filter(str.isalpha,licensePlate.lower()))
        words.sort(key=len)
        for word in words:
            if not (licensePlate - Counter(word)):
                return word