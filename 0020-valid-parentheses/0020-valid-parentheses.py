class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0] * len(s)
        top = 0
        for ch in s:
            if ch == '(':
                stack[top] = ')'
                top += 1
            elif ch == '[':
                stack[top] = ']'
                top += 1
            elif ch == '{':
                stack[top] = '}'
                top += 1
            else:
                if top == 0 or stack[top - 1] != ch:
                    return False
                top -= 1
        return top == 0