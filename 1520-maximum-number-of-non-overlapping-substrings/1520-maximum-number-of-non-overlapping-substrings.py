from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        candidates = []
        for i in range(n):
            ch = s[i]
            if first[ch] != i:
                continue

            r = last[ch]
            j = i
            valid = True
            while j <= r:
                c2 = s[j]
                if first[c2] < i:
                    valid = False
                    break
                if last[c2] > r:
                    r = last[c2]
                j += 1

            if valid:
                candidates.append((i, r))

        candidates.sort(key=lambda iv: iv[1])
        result = []
        last_end = -1
        for start, end in candidates:
            if start > last_end:
                result.append(s[start:end + 1])
                last_end = end

        return result