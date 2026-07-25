class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted((int(c) for c in str(n)), reverse=True)
        return digits[0] * digits[1]