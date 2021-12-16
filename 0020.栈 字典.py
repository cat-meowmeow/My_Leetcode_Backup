class Solution:
    def isValid(self, s: str) -> bool:
        if s=='':return True
        if len(s)==2:
            if s=='()'or s=='[]'or s=='{}':return True
            else:return False
        for i in range (len(s)):
            if len(s)%2==1:
                return False

        stack = ['?']
        d = {'(':')','[':']','{':'}','?':'?'}        
        d_re = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in d:
                stack.append(c)
            elif c in d_re and d[stack.pop()] == c: # 不需要 if c in d_re 了
                x = stack
            else:
                return False
        return x==['?']

'''
改进写法
'''
class Solution:
    def isValid(self, s: str) -> bool: #添加一个无关字符'?'来防止空栈
        stack = ['?']
        d = {'(':')','[':']','{':'}','?':'?'}        
        for bracket in s:
            if bracket in d:                # c在，入栈
                stack.append(bracket)
            else:
                l_bracket = stack.pop()
                if d[l_bracket] != bracket: # c不在，stack.pop()出栈 并判断
                    return False
        return stack == ['?']


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]: stack.pop()
                else: return False
            else: stack.append(i)           
        return not stack
