from typing import List
from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = list(accumulate(stones))  # C-level cumulative sum, faster than a manual Python loop
        dp = prefix[-1]
        for i in range(len(prefix) - 2, 0, -1):
            p = prefix[i]
            diff = p - dp
            if diff > dp:
                dp = diff
        return dp