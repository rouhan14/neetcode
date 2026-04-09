class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res = 0

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                if token == "/":
                    res = tmp2/tmp1
                    stack.append(int(res))
                elif token == "*":
                    res = tmp2*tmp1
                    stack.append(res)
                elif token == "+":
                    res = tmp1+tmp2
                    stack.append(res)
                else:
                    res = tmp2-tmp1
                    stack.append(res)
        return stack[0]