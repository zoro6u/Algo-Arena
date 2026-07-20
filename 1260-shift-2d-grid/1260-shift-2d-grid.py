from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  

        result = [[0] * n for _ in range(m)]

        for idx in range(total):
            new_idx = (idx + k) % total
            src_row, src_col = idx // n, idx % n
            new_row, new_col = new_idx // n, new_idx % n
            result[new_row][new_col] = grid[src_row][src_col]

        return result