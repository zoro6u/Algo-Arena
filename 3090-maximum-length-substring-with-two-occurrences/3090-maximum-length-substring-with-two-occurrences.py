from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        best = 0
        for right, ch in enumerate(s):
            freq[ch] += 1
            while freq[ch] > 2:               # window invalid because of the char just added
                freq[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best