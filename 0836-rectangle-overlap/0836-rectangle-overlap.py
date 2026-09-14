from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1a, y1a, x2a, y2a = rec1
        x1b, y1b, x2b, y2b = rec2
        return x1a < x2b and x1b < x2a and y1a < y2b and y1b < y2a