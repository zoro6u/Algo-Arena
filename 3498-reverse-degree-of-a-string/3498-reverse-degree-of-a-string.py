class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, start=1):
            rev_pos = 26 - (ord(ch) - ord('a'))  # 'a'->26, 'b'->25, ..., 'z'->1
            total += rev_pos * i
        return total