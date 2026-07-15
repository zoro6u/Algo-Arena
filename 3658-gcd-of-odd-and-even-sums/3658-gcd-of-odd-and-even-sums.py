class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sumOdd = n^2, sumEven = n^2 + n = n(n+1)
        # GCD(n^2, n(n+1)) = n * GCD(n, n+1) = n * 1 = n
        return n
        