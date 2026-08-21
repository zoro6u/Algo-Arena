from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        def count(x: int) -> int:
            # inclusion-exclusion over all non-empty subsets of coins
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        l = lcm(l, coins[i])
                        bits += 1
                        if l > x:  # early exit, avoids overflow/slowness
                            break
                if l > x:
                    continue
                term = x // l
                total += term if bits % 2 == 1 else -term
            return total

        lo, hi = 1, k * min(coins)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo