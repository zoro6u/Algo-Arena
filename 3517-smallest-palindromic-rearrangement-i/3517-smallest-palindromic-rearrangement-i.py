from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        
        half_chars = []
        middle = ""
        
        for ch in sorted(count.keys()):
            freq = count[ch]
            if freq % 2 == 1:
                middle = ch
            half_chars.append(ch * (freq // 2))
        
        half = "".join(half_chars)
        return half + middle + half[::-1]