from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for x in nums:
            total ^= x

        if total != 0:
            return n
        # total XOR of everything is 0; removing any single nonzero
        # element x leaves the rest XOR-ing to x (nonzero)
        if any(x != 0 for x in nums):
            return n - 1
        # every element is 0 -> every possible subset XORs to 0
        return 0