from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])

        result = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[order[j + 1]] - nums[order[j]] <= limit:
                j += 1
            group_indices = order[i:j + 1]
            group_values = [nums[k] for k in group_indices]
            group_values.sort()
            sorted_positions = sorted(group_indices)
            for pos, val in zip(sorted_positions, group_values):
                result[pos] = val
            i = j + 1

        return result