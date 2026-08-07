class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                       # no zigzag possible; also avoids a
            return s                           # meaningless period below

        rows = [''] * numRows                  # one string buffer per row
        current_row = 0
        direction = -1                          # flips to +1 on the very first char

        for c in s:
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1                # bounce off top/bottom BEFORE moving
            rows[current_row] += c
            current_row += direction

        return ''.join(rows)