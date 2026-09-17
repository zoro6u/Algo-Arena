class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # dp[i] = أقصر subarray مجموعها target
        # موجودة في arr[0:i]
        dp = [float('inf')] * (n + 1)

        prefix = 0
        seen = {0: -1}

        answer = float('inf')

        for i in range(n):
            prefix += arr[i]

            # أقصر subarray موجودة قبل i
            dp[i + 1] = dp[i]

            if prefix - target in seen:
                start = seen[prefix - target]
                length = i - start

                # هل في subarray سابقة غير متداخلة؟
                if dp[start + 1] != float('inf'):
                    answer = min(
                        answer,
                        length + dp[start + 1]
                    )

                # نحدث أقصر subarray تنتهي هنا
                dp[i + 1] = min(dp[i + 1], length)

            seen[prefix] = i

        return answer if answer != float('inf') else -1