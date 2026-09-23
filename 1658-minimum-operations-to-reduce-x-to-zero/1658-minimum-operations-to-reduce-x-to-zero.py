from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        left = 0
        window_sum = 0
        best_len = -1

        for right in range(n):
            window_sum += nums[right]
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                best_len = max(best_len, right - left + 1)

        return n - best_len if best_len != -1 else -1