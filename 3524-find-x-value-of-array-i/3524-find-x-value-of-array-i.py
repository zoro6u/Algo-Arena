from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        f = [0] * k  # f[r] = number of subarrays ENDING at current position with product % k == r

        for num in nums:
            val = num % k
            new_f = [0] * k
            for r in range(k):
                if f[r]:
                    new_f[(r * val) % k] += f[r]
            new_f[val] += 1
            f = new_f
            for r in range(k):
                result[r] += f[r]

        return result