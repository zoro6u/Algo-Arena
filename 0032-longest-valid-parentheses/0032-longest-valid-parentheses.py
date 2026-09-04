class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, best = [-1], 0
        for i, c in enumerate(s): stack.append(i) if c=='(' else (stack.pop(), stack.append(i) if not stack else (best := max(best, i-stack[-1])))
        return best