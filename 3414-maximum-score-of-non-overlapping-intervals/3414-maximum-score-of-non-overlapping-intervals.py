from typing import List
import bisect

class Gap:
    __slots__ = ('lo', 'hi', 'cands', 'starts', 'suffix_dp',
                 'cands_by_r', 'ends_by_r', 'prefix_dp', 'best')

    def __init__(self, lo, hi, cands, budget):
        self.lo = lo
        self.hi = hi
        self.cands = sorted(cands, key=lambda x: x[0])
        m = len(self.cands)
        self.starts = [c[0] for c in self.cands]

        suffix_dp = [[0] * (budget + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            l, r, w, idx = self.cands[i]
            nxt = bisect.bisect_right(self.starts, r)
            for k in range(budget + 1):
                suffix_dp[i][k] = suffix_dp[i + 1][k]
                if k >= 1:
                    suffix_dp[i][k] = max(suffix_dp[i][k], w + suffix_dp[nxt][k - 1])
        self.suffix_dp = suffix_dp
        self.best = suffix_dp[0]

        self.cands_by_r = sorted(cands, key=lambda x: x[1])
        self.ends_by_r = [c[1] for c in self.cands_by_r]

        prefix_dp = [[0] * (budget + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            l, r, w, idx = self.cands_by_r[i - 1]
            prv = bisect.bisect_left(self.ends_by_r, l, 0, i - 1)
            for k in range(budget + 1):
                prefix_dp[i][k] = prefix_dp[i - 1][k]
                if k >= 1:
                    prefix_dp[i][k] = max(prefix_dp[i][k], w + prefix_dp[prv][k - 1])
        self.prefix_dp = prefix_dp

    def split_query(self, l, r, budget):
        left_pos = bisect.bisect_left(self.ends_by_r, l)
        left_best = self.prefix_dp[left_pos]
        right_pos = bisect.bisect_right(self.starts, r)
        right_best = self.suffix_dp[right_pos]
        return left_best, right_best


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        items = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        NEG_INF = float('-inf')
        BUDGET = 4

        initial_gap = Gap(NEG_INF, float('inf'), items, BUDGET)
        target = initial_gap.best[BUDGET]
        if target == 0:
            return []

        active_gaps = [initial_gap]
        selected = []
        remaining_budget = BUDGET
        score_so_far = 0

        def other_gaps_best_sum(exclude_gap, budget):
            best = [0] * (budget + 1)
            for g in active_gaps:
                if g is exclude_gap:
                    continue
                new_best = [0] * (budget + 1)
                for total in range(budget + 1):
                    new_best[total] = max(best[j] + g.best[total - j] for j in range(total + 1))
                best = new_best
            return best

        for i in range(n):
            if remaining_budget == 0:
                break
            l, r, w, idx = items[i]

            host = None
            for g in active_gaps:
                if g.lo < l and r < g.hi:
                    host = g
                    break
            if host is None:
                continue

            left_best, right_best = host.split_query(l, r, remaining_budget - 1)
            others_best = other_gaps_best_sum(host, remaining_budget - 1)

            achievable = 0
            for b_left in range(remaining_budget):
                for b_right in range(remaining_budget - b_left):
                    b_other = remaining_budget - 1 - b_left - b_right
                    if b_other < 0:
                        continue
                    val = left_best[b_left] + right_best[b_right] + others_best[b_other]
                    achievable = max(achievable, val)

            if score_so_far + w + achievable == target:
                active_gaps.remove(host)
                left_cands = [c for c in host.cands if c[1] < l]
                right_cands = [c for c in host.cands if c[0] > r]
                if left_cands:
                    active_gaps.append(Gap(host.lo, l, left_cands, remaining_budget - 1))
                if right_cands:
                    active_gaps.append(Gap(r, host.hi, right_cands, remaining_budget - 1))
                active_gaps.sort(key=lambda g: g.lo)

                selected.append((l, r, w, idx))
                score_so_far += w
                remaining_budget -= 1

        return sorted(c[3] for c in selected)