'''
回溯：循环里嵌套递归      深度优先遍历中的状态重置，depth，path，used(bool)
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":return[]

        phone = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}

        def backtrack(com,nextdigit):
            if len(nextdigit)==0:
                res.append(com)
            else:
                for l in phone[nextdigit[0]]:
                    backtrack(com+l,nextdigit[1:])
        
        res = []
        backtrack('',digits)
        return res
'''
队列
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit)-50]:# 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue
'''
