from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in order]
        pos = [0] * n
        for p, node in enumerate(order):
            pos[node] = p

        reach = [0] * n
        r = 0
        for i in range(n):
            if r < i:
                r = i
            while r + 1 < n and sorted_vals[r + 1] - sorted_vals[i] <= maxDiff:
                r += 1
            reach[i] = r

        comp = [0] * n
        cur_id = 0
        max_reach = -1
        for i in range(n):
            if i > max_reach:
                cur_id += 1
                max_reach = reach[i]
            else:
                max_reach = max(max_reach, reach[i])
            comp[i] = cur_id

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        up[0] = reach[:]
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for i in range(n):
                cur[i] = prev[prev[i]]

        def min_hops(pu: int, pv: int) -> int:
            if pu == pv:
                return 0
            if pu > pv:
                pu, pv = pv, pu
            if comp[pu] != comp[pv]:
                return -1
            steps = 0
            i = pu
            for k in range(LOG - 1, -1, -1):
                if up[k][i] < pv:
                    i = up[k][i]
                    steps += (1 << k)
            steps += 1
            return steps

        ans = []
        for u, v in queries:
            ans.append(min_hops(pos[u], pos[v]))
        return ans