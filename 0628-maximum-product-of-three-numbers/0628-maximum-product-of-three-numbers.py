class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Track the three largest and the two smallest in one pass.
        max1 = max2 = max3 = float('-inf')   # max1 >= max2 >= max3
        min1 = min2 = float('inf')           # min1 <= min2

        for n in nums:
            # update largest three
            if n >= max1:
                max1, max2, max3 = n, max1, max2
            elif n >= max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
            # update smallest two
            if n <= min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n

        return max(max1 * max2 * max3, min1 * min2 * max1)