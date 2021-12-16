class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':    #   stack.append(stack[-1]*2)
                last = stack.pop()  # 直接算，别pop了
                last2 = last*2
                stack.append(last)
                stack.append(last2)
            elif op == '+':   #   stack.append(stack[-1] + stack[-2])
                a = stack.pop()
                b = stack.pop()
                c = a+b
                stack.append(b)
                stack.append(a)
                stack.append(c)
            else:
                stack.append(int(op))
        return sum(stack)
