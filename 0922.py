class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even,odd,nums = [],[],[]
        for i in A:
            if i&1 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(even)):
            nums.append(even[i])
            nums.append(odd[i])
        return nums
