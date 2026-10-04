class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0