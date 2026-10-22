from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        p = nums.index(0)                       # position of 0
        asc = all(nums[(p + j) % n] == j for j in range(n))
        desc = all(nums[(p - j) % n] == j for j in range(n))
        if not asc and not desc:
            return -1
        best = float('inf')
        if asc:
            # rotate left p times, or reverse + rotate left (n-p) + reverse
            best = min(best, 0 if p == 0 else min(p, n - p + 2))
        if desc:
            # one reverse, then fix the rotation (either direction)
            k = (p + 1) % n
            best = min(best, 1 + min(k, n - k))
        return best