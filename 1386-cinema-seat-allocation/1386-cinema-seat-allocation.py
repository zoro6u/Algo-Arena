from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_mask = defaultdict(int)
        for row, seat in reservedSeats:
            row_mask[row] |= (1 << seat)

        LEFT  = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        MID   = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        RIGHT = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        total = (n - len(row_mask)) * 2   # untouched rows fit 2 groups each

        for row, mask in row_mask.items():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                total += 2
            elif (mask & LEFT) == 0 or (mask & MID) == 0 or (mask & RIGHT) == 0:
                total += 1

        return total