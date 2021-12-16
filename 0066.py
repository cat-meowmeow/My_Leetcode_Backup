class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        n = l-1             


        for i in range(l-1,-1,-1):
            if  digits[l-1] != 9:
                digits[l-1] = digits[l-1]+1
            else:
                while digits[n] == 9:
                    digits[n] = 0
                    n = n-1
                digits[n] = digits[n]+1
            return digits
