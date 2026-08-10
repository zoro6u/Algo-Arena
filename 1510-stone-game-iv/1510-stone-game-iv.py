class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = True if the player about to move with i stones wins
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:   # found a move that dumps a loss on the opponent
                    dp[i] = True
                    break
                j += 1
        return dp[n]