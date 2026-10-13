from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted((x * x for x in nums), reverse=True)
        plus = (len(sq) + 1) // 2   # even indices 0,2,4,... get +
        return sum(sq[:plus]) - sum(sq[plus:])