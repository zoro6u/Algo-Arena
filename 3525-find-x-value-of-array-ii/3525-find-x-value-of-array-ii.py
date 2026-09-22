class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        # per node: product mod k, and C[j] = how many of its own non-empty prefixes
        # have product == j (mod k)
        P = [1] * (2 * size)
        C = [0] * (2 * size * k)
        for i in range(n):
            vm = nums[i] % k
            P[size + i] = vm
            C[(size + i) * k + vm] = 1

        def pull(nd):
            l = nd << 1
            r = l | 1
            pl = P[l]
            P[nd] = pl * P[r] % k
            base = nd * k
            bl = l * k
            br = r * k
            for j in range(k):
                C[base + j] = C[bl + j]
            for j in range(k):
                v = C[br + j]
                if v:
                    C[base + pl * j % k] += v

        for nd in range(size - 1, 0, -1):
            pull(nd)

        out = []
        for idx, val, start, x in queries:
            leaf = size + idx
            vm = val % k
            if P[leaf] != vm:
                base = leaf * k
                for j in range(k):
                    C[base + j] = 0
                C[base + vm] = 1
                P[leaf] = vm
                nd = leaf >> 1
                while nd:
                    pull(nd)
                    nd >>= 1

            lo = start + size
            hi = n + size
            left = []
            right = []
            while lo < hi:
                if lo & 1:
                    left.append(lo)
                    lo += 1
                if hi & 1:
                    hi -= 1
                    right.append(hi)
                lo >>= 1
                hi >>= 1
            right.reverse()
            cur = 1 % k
            res = 0
            for nd in left + right:
                base = nd * k
                for j in range(k):
                    if cur * j % k == x:
                        res += C[base + j]
                cur = cur * P[nd] % k
            out.append(res)
        return out