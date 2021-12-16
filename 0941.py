class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        num = arr[0]
        i = 1
        n =len(arr)
        if n < 3:return False
        if n == 3:
            if arr[0]<arr[1] and arr[1]>arr[2]: return True
            else: return False
        while i < n-1:
            if num == arr[i]:return False
            elif num < arr[i]:
                num = arr[i]
                i += 1
            else:
                num = arr[i]
                i = i+1
                break
        while i < n:
            if num <= arr[i] or i == 2:return False
            else:
                num = arr[i]
                i += 1
        return True
