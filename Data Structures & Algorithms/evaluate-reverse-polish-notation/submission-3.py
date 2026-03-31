class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                temp = stack.pop()
                temp2 = stack.pop()
                if token == '/':
                    res = int(temp2 / temp)
                    stack.append(res)
                elif token == '*':
                    res = temp * temp2
                    stack.append(res)
                elif token == '-':
                    res = temp2 - temp
                    stack.append(res)
                elif token == '+':
                    res = temp + temp2
                    stack.append(res)
        return stack[0]