from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                total += nums[i - 1] ** 2
                j = n // i
                if j != i:
                    total += nums[j - 1] ** 2
            i += 1
        return total