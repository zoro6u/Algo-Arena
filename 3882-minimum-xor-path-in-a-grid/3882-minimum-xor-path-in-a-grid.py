from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # reach[j] = set of XOR values achievable at the current row, column j
        reach = [None] * n
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    reach[0] = {v}
                    continue
                prev = set()
                if i > 0:
                    prev |= reach[j]            # coming from above (previous row's value of this column)
                if j > 0:
                    prev |= reach[j - 1]        # coming from the left (already updated this row)
                reach[j] = {x ^ v for x in prev}
        return min(reach[n - 1])