class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def total(k: int) -> int:
            # buy k "both" items, then cover whatever is still missing with single-type items
            return k * costBoth + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2
        # total(k) is piecewise linear in k, so its minimum is at a breakpoint
        return min(total(0), total(min(need1, need2)), total(max(need1, need2)))