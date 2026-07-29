from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        odd_chars = [c for c, cnt in freq.items() if cnt % 2 == 1]
        middle = odd_chars[0] if odd_chars else ''

        half_counts = {c: cnt // 2 for c, cnt in freq.items() if cnt // 2 > 0}
        half_length = sum(half_counts.values())

        def comb_capped(n, r, cap):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            result = 1
            for i in range(r):
                result = result * (n - i) // (i + 1)
                if result > cap:
                    return cap + 1
            return result

        def count_perms_capped(counts, length, cap):
            result = 1
            remaining = length
            for cnt in counts.values():
                if cnt == 0:
                    continue
                c = comb_capped(remaining, cnt, cap)
                result *= c
                remaining -= cnt
                if result > cap:
                    return cap + 1
            return result

        if k <= 0:
            return ""

        total = count_perms_capped(half_counts, half_length, k)
        if total < k:
            return ""

        result_chars = []
        counts = dict(half_counts)
        remaining = half_length

        for _ in range(half_length):
            for c in sorted(counts.keys()):
                if counts[c] == 0:
                    continue
                counts[c] -= 1
                cnt = count_perms_capped(counts, remaining - 1, k)
                if k <= cnt:
                    result_chars.append(c)
                    remaining -= 1
                    break
                else:
                    k -= cnt
                    counts[c] += 1

        half_str = ''.join(result_chars)
        return half_str + middle + half_str[::-1]