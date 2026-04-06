class Solution:
    def isValid(self, s: str) -> bool:

        check = {"(": ")", "{": "}", "[": "]"}
        
        stack = []

        for char in s:

            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                if char != check[stack.pop()]:
                    return False
        
        return not stack
