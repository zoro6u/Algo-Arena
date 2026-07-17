from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxVal = max(nums)
        
        # 1. frequency of each value
        freq = [0] * (maxVal + 1)
        for x in nums:
            freq[x] += 1
        
        # 2. count of elements divisible by v, for each v
        cntMultiple = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            total = 0
            for m in range(v, maxVal + 1, v):
                total += freq[m]
            cntMultiple[v] = total
        
        # 3. pairs where both elements divisible by v
        pairCount = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            c = cntMultiple[v]
            pairCount[v] = c * (c - 1) // 2
        
        # 4. inclusion-exclusion to get exact GCD counts
        exact = pairCount[:]  # copy
        for v in range(maxVal, 0, -1):
            for m in range(2 * v, maxVal + 1, v):
                exact[v] -= exact[m]
        
        # 5. prefix sum: prefix[g] = number of pairs with gcd <= g
        prefix = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            prefix[v] = prefix[v - 1] + exact[v]
        
        # 6. answer queries with binary search
        answer = []
        for q in queries:
            g = bisect_right(prefix, q)  # smallest g with prefix[g] > q
            answer.append(g)
        
        return answer