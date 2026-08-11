from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        # find the longest sequential prefix and its sum
        prefix_sum = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1

        # smallest x >= prefix_sum that's not present in nums
        present = set(nums)
        x = prefix_sum
        while x in present:
            x += 1
        return x