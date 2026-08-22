class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        temp = n
        while temp > 0:
            d = temp % 10
            digit_sum += d
            digit_product *= d
            temp //= 10
        return n % (digit_sum + digit_product) == 0