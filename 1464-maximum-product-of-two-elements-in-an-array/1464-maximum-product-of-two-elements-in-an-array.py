class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0  # max1 >= max2; all nums >= 1 so 0 is a safe floor
        for n in nums:
            if n >= max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)