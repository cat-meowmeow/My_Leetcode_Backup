class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in {6, 28, 496, 8128, 33550336}

'''
        num_facts = [1]
        for i in range(2,num):
            if num % i == 0:
                j = num//i
                if i < j:
                    num_facts.append(i)
                    num_facts.append(j)
                elif i == j:
                    num_facts.append(i)
                    break
                else:
                    break   
        return num==sum(num_facts)
'''
