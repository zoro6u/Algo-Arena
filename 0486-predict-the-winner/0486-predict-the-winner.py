class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        # dp[i][j] = max score difference (current player - opponent)
        # achievable when only nums[i..j] remains
        dp = [[0] * n for _ in range(n)]

        # base case: single element
        for i in range(n):
            dp[i][i] = nums[i]

        # fill by increasing subarray length
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                take_left = nums[i] - dp[i + 1][j]
                take_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(take_left, take_right)

        return dp[0][n - 1] >= 0