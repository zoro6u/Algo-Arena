class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines, rest = divmod(sum, 9)
        out = "9" * nines
        if rest:
            out += str(rest)
        return out + "0" * (num - len(out))