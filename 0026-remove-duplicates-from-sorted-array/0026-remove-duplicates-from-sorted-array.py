from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # index where the next unique value should be written
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:   # new unique value found
                nums[k] = nums[i]
                k += 1
        return k