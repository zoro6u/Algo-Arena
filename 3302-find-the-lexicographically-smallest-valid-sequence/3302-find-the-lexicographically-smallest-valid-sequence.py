class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []

        # suf[i] = how many chars of word2, counted from its END, can still be
        # matched as a subsequence inside word1[i:]
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            k = suf[i + 1]
            suf[i] = k + 1 if k < m and word1[i] == word2[m - 1 - k] else k

        res = []
        j = 0            # next position of word2 to fill
        used = False     # has the single allowed change been spent?
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                res.append(i)                    # free match, budget untouched
                j += 1
            elif not used and suf[i + 1] >= m - j - 1:
                res.append(i)                    # spend the one change here
                j += 1
                used = True
        return res if j == m else []