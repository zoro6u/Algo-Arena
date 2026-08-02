class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]  # dp[j] represents dp[i][j] for current row i

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])

        return dp[n - 1] > 0