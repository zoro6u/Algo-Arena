from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from index i to the end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def best(i: int, m: int) -> int:
            # can sweep the rest of the board legally -> take it all
            if i + 2 * m >= n:
                return suffix[i]
            # take x piles; opponent optimally takes best(...); the rest is mine
            return max(
                suffix[i] - best(i + x, max(m, x))
                for x in range(1, 2 * m + 1)
            )

        ans = best(0, 1)
        best.cache_clear()   # avoid the cache leaking across test cases
        return ans