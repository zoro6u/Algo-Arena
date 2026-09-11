from typing import List
from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        seen = set()
        for i, j, k in permutations(range(n), 3):
            if digits[i] == 0:
                continue
            if digits[k] % 2 != 0:
                continue
            num = digits[i] * 100 + digits[j] * 10 + digits[k]
            seen.add(num)
        return len(seen)