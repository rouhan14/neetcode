class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for brack in s:
            if brack in '({[':
                stack.append(brack)
            else:
                if not stack or stack[-1] != mapping[brack]:
                    return False
                stack.pop()

        return len(stack) == 0
