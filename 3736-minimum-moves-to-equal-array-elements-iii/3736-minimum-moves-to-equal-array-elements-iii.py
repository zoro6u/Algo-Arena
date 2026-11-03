from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        top = max(nums)
        return sum(top - x for x in nums)