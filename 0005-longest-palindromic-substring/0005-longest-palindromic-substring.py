class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, length = 0, 1          # s is non-empty, so 1 char is always a valid answer

        def expand(left: int, right: int) -> None:
            nonlocal start, length
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # loop overshot by one on each side => palindrome is s[left+1 : right]
            width = right - left - 1
            if width > length:
                start, length = left + 1, width

        for i in range(n):
            expand(i, i)              # odd-length: centered on s[i]
            expand(i, i + 1)          # even-length: centered between s[i] and s[i+1]

        return s[start:start + length]