from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def ds(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        n = len(nums)
        order = sorted(range(n), key=lambda i: (ds(nums[i]), nums[i]))
        seen = [False] * n
        swaps = 0
        for i in range(n):
            if seen[i] or order[i] == i:
                continue
            length = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = order[j]
                length += 1
            swaps += length - 1
        return swaps