from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        best = 0
        for right, x in enumerate(nums):
            freq[x] += 1
            while freq[x] > k:              # window invalid because of the element just added
                freq[nums[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best