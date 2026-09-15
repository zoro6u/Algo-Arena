class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0

        def is_palindrome(i, j):
            lo, hi = i, j - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            for length in (k, k + 1):
                if i + length <= n and is_palindrome(i, i + length):
                    dp[i] = max(dp[i], 1 + dp[i + length])

        return dp[0]