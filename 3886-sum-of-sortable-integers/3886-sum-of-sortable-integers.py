from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = float('-inf')
            for s in range(0, n, k):
                block = nums[s:s + k]
                # a block is a rotation of a sorted block iff it has <= 1 cyclic descent
                descents = sum(1 for i in range(k) if block[i] > block[(i + 1) % k])
                if descents > 1 or min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)
            if ok:
                total += k
        return total