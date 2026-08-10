class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        # build the LPS (longest proper prefix which is also suffix) table
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]   # fall back within needle, don't lose progress
            else:
                lps[i] = 0
                i += 1

        # scan haystack using the table to avoid re-checking matched characters
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j          # full match found, report its start
            elif j != 0:
                j = lps[j - 1]            # reuse partial match info
            else:
                i += 1
        return -1