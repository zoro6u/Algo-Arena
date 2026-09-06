class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n:
            return 0

        dp = [0] * (m + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            ch = s[i - 1]
            for j in range(min(i, m), 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
        