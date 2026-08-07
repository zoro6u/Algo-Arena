from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # ---- Step 1: factor t into 2^a * 3^b * 5^c * 7^d * r ----
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

        REQ = (a, b, c, d)

        # exponent contribution of each digit 1..9
        DIGIT = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0),
        }

        def sub(req, dv):
            return (max(req[0] - dv[0], 0), max(req[1] - dv[1], 0),
                    max(req[2] - dv[2], 0), max(req[3] - dv[3], 0))

        # ---- Step 2: minLen[req] = min digits to satisfy remaining req ----
        @lru_cache(maxsize=None)
        def min_len(req):
            if req == (0, 0, 0, 0):
                return 0
            best = None
            for dig in range(1, 10):
                nxt = sub(req, DIGIT[dig])
                if nxt == req:  # digit 1 contributes nothing, avoid infinite loop
                    continue
                cand = 1 + min_len(nxt)
                if best is None or cand < best:
                    best = cand
            return best

        def feasible(req, length):
            return min_len(req) <= length

        # ---- Step 3: build smallest zero-free suffix of given length meeting req ----
        def smallest_suffix(length, req):
            res = []
            for _ in range(length):
                length -= 1
                for dig in range(1, 10):
                    nxt = sub(req, DIGIT[dig])
                    if feasible(nxt, length):
                        res.append(str(dig))
                        req = nxt
                        break
            return "".join(res)

        n = len(num)
        digits = [int(ch) for ch in num]

        # quick check: num itself already valid?
        if 0 not in digits:
            req = REQ
            for dig in digits:
                req = sub(req, DIGIT[dig])
            if req == (0, 0, 0, 0):
                return num

        # first zero position (or n if none) -> tight prefix can't pass it
        p = n
        for i, dig in enumerate(digits):
            if dig == 0:
                p = i
                break

        # prefix exponent contribution up to (not including) index i, for i = 0..p
        prefix_req = [REQ]
        cur = REQ
        for i in range(p):
            cur = sub(cur, DIGIT[digits[i]])
            prefix_req.append(cur)

        limit = min(p, n - 1)
        for i in range(limit, -1, -1):
            base_req = prefix_req[i]
            start = digits[i] + 1
            for dig in range(start, 10):
                nxt = sub(base_req, DIGIT[dig])
                remaining_len = n - 1 - i
                if feasible(nxt, remaining_len):
                    prefix_str = num[:i] + str(dig)
                    return prefix_str + smallest_suffix(remaining_len, nxt)

        # ---- Step 5: fall back to length n+1 (or more if needed) ----
        L = max(n + 1, min_len(REQ))
        return smallest_suffix(L, REQ)