from itertools import product

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def factor_out(x, p):
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            return x, e

        r = t
        r, a = factor_out(r, 2)
        r, b = factor_out(r, 3)
        r, c = factor_out(r, 5)
        r, d = factor_out(r, 7)
        if r != 1:
            return "-1"

        A, B, C, D = a + 1, b + 1, c + 1, d + 1
        total = A * B * C * D

        DIGIT = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0),
        }

        def encode(x2, x3, x5, x7):
            return ((x2 * B + x3) * C + x5) * D + x7

        START = encode(a, b, c, d)
        ZERO = encode(0, 0, 0, 0)  # == 0

        # ---- precompute transitions once (small, independent of n) ----
        trans = [[0] * 9 for _ in range(total)]
        for x2, x3, x5, x7 in product(range(A), range(B), range(C), range(D)):
            s = encode(x2, x3, x5, x7)
            row = trans[s]
            for dig in range(1, 10):
                e2, e3, e5, e7 = DIGIT[dig]
                nx2 = x2 - e2 if x2 > e2 else 0
                nx3 = x3 - e3 if x3 > e3 else 0
                nx5 = x5 - e5 if x5 > e5 else 0
                nx7 = x7 - e7 if x7 > e7 else 0
                row[dig - 1] = encode(nx2, nx3, nx5, nx7)

        # ---- min_len via bottom-up DP (ascending order = topological order) ----
        INF = float('inf')
        min_len = [0] * total
        for x2, x3, x5, x7 in product(range(A), range(B), range(C), range(D)):
            s = encode(x2, x3, x5, x7)
            if s == ZERO:
                continue
            best = INF
            row = trans[s]
            for dig in range(9):
                ns = row[dig]
                if ns == s:
                    continue
                v = 1 + min_len[ns]
                if v < best:
                    best = v
            min_len[s] = best

        def smallest_suffix(length, state):
            res = []
            rem = length
            for _ in range(length):
                rem -= 1
                row = trans[state]
                for dig in range(1, 10):
                    ns = row[dig - 1]
                    if min_len[ns] <= rem:
                        res.append(str(dig))
                        state = ns
                        break
            return "".join(res)

        n = len(num)
        digits = [int(ch) for ch in num]

        if 0 not in digits:
            state = START
            for dig in digits:
                state = trans[state][dig - 1]
            if state == ZERO:
                return num

        p = n
        for i, dig in enumerate(digits):
            if dig == 0:
                p = i
                break

        prefix_state = [START]
        state = START
        for i in range(p):
            state = trans[state][digits[i] - 1]
            prefix_state.append(state)

        limit = min(p, n - 1)
        for i in range(limit, -1, -1):
            row = trans[prefix_state[i]]
            for dig in range(digits[i] + 1, 10):
                ns = row[dig - 1]
                remaining_len = n - 1 - i
                if min_len[ns] <= remaining_len:
                    return num[:i] + str(dig) + smallest_suffix(remaining_len, ns)

        L = max(n + 1, min_len[START])
        return smallest_suffix(L, START)