class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x: int) -> int:
            product = 1
            while x > 0:
                product *= x % 10
                x //= 10
            return product

        candidate = n
        while digit_product(candidate) % t != 0:
            candidate += 1
        return candidate