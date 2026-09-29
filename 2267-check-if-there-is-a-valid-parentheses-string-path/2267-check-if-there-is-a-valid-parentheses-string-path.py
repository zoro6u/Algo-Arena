from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] != '(' or grid[m-1][n-1] != ')':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0] = {1}

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                delta = 1 if grid[r][c] == '(' else -1
                balances = set()
                if r > 0:
                    for b in dp[r-1][c]:
                        nb = b + delta
                        if nb >= 0:
                            balances.add(nb)
                if c > 0:
                    for b in dp[r][c-1]:
                        nb = b + delta
                        if nb >= 0:
                            balances.add(nb)
                dp[r][c] = balances

        return 0 in dp[m-1][n-1]