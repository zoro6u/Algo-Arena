class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] = best (current player's score - opponent's score) for stones i..n-1
        dp = [0] * (n + 1)          # dp[n] = 0: no stones left, nobody ahead

        for i in range(n - 1, -1, -1):
            taken = 0
            best = float('-inf')    # NOT 0: taking is mandatory, values can be negative
            for k in range(3):      # take 1, 2, or 3 stones
                if i + k >= n:      # can't take past the end of the row
                    break
                taken += stoneValue[i + k]
                # what I grab now, minus the lead my opponent gets from what's left
                best = max(best, taken - dp[i + k + 1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"