from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        m = min(nums1)
        if m % 2 != 0:
            return True  # minimum is odd -> always achievable
        return all(x % 2 == 0 for x in nums1)  # minimum is even -> only OK if no odd numbers exist