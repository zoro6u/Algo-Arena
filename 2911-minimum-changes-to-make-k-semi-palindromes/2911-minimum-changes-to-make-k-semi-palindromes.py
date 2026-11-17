from typing import List

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")
        divs = [[d for d in range(1, L) if L % d == 0] for L in range(n + 1)]
        # cost[i][j] = min changes to make s[i..j] a semi-palindrome (INF for length 1)
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divs[L]:
                    c = 0
                    for g in range(d):                 # each residue group must be a palindrome
                        lo, hi = i + g, j - d + 1 + g  # first and last element of the group
                        while lo < hi:
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                    if c < best:
                        best = c
                cost[i][j] = best
        # dp[p][i] = min cost to split the first i chars into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                best = INF
                for m in range(2 * (p - 1), i - 1):    # last part is s[m..i-1], length >= 2
                    v = dp[p - 1][m] + cost[m][i - 1]
                    if v < best:
                        best = v
                dp[p][i] = best
        return dp[k][n]