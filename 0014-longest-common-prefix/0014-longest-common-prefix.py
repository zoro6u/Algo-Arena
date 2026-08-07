class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        min_len = len(first)
        for s in strs[1:]:
            if len(s) < min_len:
                min_len = len(s)

        lo, hi = 0, min_len
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            ok = True
            prefix = first[:mid]
            for s in strs:
                if not s.startswith(prefix):
                    ok = False
                    break
            if ok:
                lo = mid
            else:
                hi = mid - 1
        return first[:lo]