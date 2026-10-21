class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = sorted(s)
        if s == "".join(t):
            return 0
        if n == 2:
            return -1                      # only single-character substrings can be chosen
        lo, hi = t[0], t[-1]
        if s[0] == lo or s[-1] == hi:
            return 1                       # sort everything except the already-correct end
        if lo in s[:-1] or hi in s[1:]:
            return 2
        return 3