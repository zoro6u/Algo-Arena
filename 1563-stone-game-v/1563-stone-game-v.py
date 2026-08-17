from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rangeSum(a, b):
            return prefix[b + 1] - prefix[a]

        NEG = float('-inf')
        dp = [[0] * n for _ in range(n)]

        leftPtr = list(range(n))
        leftRunMax = [NEG] * n
        rightPtr = list(range(n))
        rightRunMax = [NEG] * n

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                while leftPtr[i] <= j - 1 and rangeSum(i, leftPtr[i]) <= rangeSum(leftPtr[i] + 1, j):
                    k = leftPtr[i]
                    leftRunMax[i] = max(leftRunMax[i], rangeSum(i, k) + dp[i][k])
                    leftPtr[i] += 1

                while rightPtr[j] >= i + 1 and rangeSum(rightPtr[j], j) <= rangeSum(i, rightPtr[j] - 1):
                    m = rightPtr[j]
                    rightRunMax[j] = max(rightRunMax[j], rangeSum(m, j) + dp[m][j])
                    rightPtr[j] -= 1

                dp[i][j] = max(leftRunMax[i], rightRunMax[j])

        return dp[0][n - 1]