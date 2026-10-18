from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # Pascal's triangle: C[i][j] = i choose j (mod MOD)
        C = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
        result = 1
        stack = [nums]
        while stack:
            arr = stack.pop()
            if len(arr) <= 2:
                continue
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            result = result * C[len(arr) - 1][len(left)] % MOD
            stack.append(left)
            stack.append(right)
        return (result - 1) % MOD   # exclude the original ordering