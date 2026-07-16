from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefix_gcd[i] = gcd(nums[i], mx)
        
        prefix_gcd.sort()
        
        total = 0
        left, right = 0, n - 1
        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        
        return total