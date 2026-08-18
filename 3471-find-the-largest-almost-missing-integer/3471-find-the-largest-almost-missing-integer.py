from typing import List
from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        positions = defaultdict(list)
        for i, x in enumerate(nums):
            positions[x].append(i)

        best = -1
        for x, ps in positions.items():
            # merge the window-start ranges [max(0,p-k+1), min(p, n-k)] for each occurrence p
            total_covered = 0
            cur_lo, cur_hi = None, None
            for p in ps:
                lo = max(0, p - k + 1)
                hi = min(p, n - k)
                if cur_lo is None:
                    cur_lo, cur_hi = lo, hi
                elif lo <= cur_hi + 1:            # overlapping or touching -> merge
                    cur_hi = max(cur_hi, hi)
                else:
                    total_covered += cur_hi - cur_lo + 1
                    cur_lo, cur_hi = lo, hi
                if total_covered > 1:
                    break                          # already disqualified, stop early
            if cur_lo is not None:
                total_covered += cur_hi - cur_lo + 1

            if total_covered == 1:
                best = max(best, x)

        return best