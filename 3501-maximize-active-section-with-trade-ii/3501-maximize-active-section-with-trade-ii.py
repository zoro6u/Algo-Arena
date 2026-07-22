from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '1' else 0)

        whole_total = prefix[n]   # answer is always relative to the WHOLE string's count

        runs = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            runs.append((s[i], i, j))
            i = j + 1
        m = len(runs)
        run_starts = [r[1] for r in runs]

        def find_run(pos):
            lo, hi = 0, m - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if run_starts[mid] <= pos:
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        NEG, POS = float('-inf'), float('inf')

        def run_len(idx):
            ch, st, en = runs[idx]
            return en - st + 1

        zero_len_arr = [(en - st + 1) if ch == '0' else NEG for (ch, st, en) in runs]
        one_len_arr = [(en - st + 1) if ch == '1' else POS for (ch, st, en) in runs]
        # gain from removing run i and merging its zero neighbors
        merge_val_arr = [NEG] * m
        for idx in range(m):
            if runs[idx][0] == '1' and idx - 1 >= 0 and idx + 1 < m:
                merge_val_arr[idx] = run_len(idx - 1) + run_len(idx + 1)

        def build_sparse(arr, op):
            n_ = len(arr)
            if n_ == 0:
                return []
            table = [arr[:]]
            j = 1
            while (1 << j) <= n_:
                prev = table[-1]
                half = 1 << (j - 1)
                cur = [op(prev[i], prev[i + half]) for i in range(n_ - (1 << j) + 1)]
                table.append(cur)
                j += 1
            return table

        max_table = build_sparse(zero_len_arr, max) if m > 0 else []
        min_table = build_sparse(one_len_arr, min) if m > 0 else []
        merge_table = build_sparse(merge_val_arr, max) if m > 0 else []

        def query_op(table, l, r, op, default):
            if l > r:
                return default
            length = r - l + 1
            k = length.bit_length() - 1
            return op(table[k][l], table[k][r - (1 << k) + 1])

        def query_max(table, l, r):
            return query_op(table, l, r, max, NEG)

        def query_min(table, l, r):
            return query_op(table, l, r, min, POS)

        ans = []
        for (l, r) in queries:
            rid_l = find_run(l)
            rid_r = find_run(r)

            if rid_l == rid_r:
                ans.append(whole_total)
                continue

            left_ch, left_st, left_en = runs[rid_l]
            left_len = left_en - l + 1
            right_ch, right_st, right_en = runs[rid_r]
            right_len = r - right_st + 1

            # independent max zero block (fill target unrelated to which 1-block is removed)
            full_max_zero = query_max(max_table, rid_l + 1, rid_r - 1) if rid_l + 1 <= rid_r - 1 else NEG
            candidates = [full_max_zero]
            if left_ch == '0':
                candidates.append(left_len)
            if right_ch == '0':
                candidates.append(right_len)
            best_zero = max(candidates)
            if best_zero == NEG:
                best_zero = 0

            # independent min one block (strictly interior)
            best_one_remove = None
            if rid_l + 1 <= rid_r - 1:
                mn = query_min(min_table, rid_l + 1, rid_r - 1)
                if mn != POS:
                    best_one_remove = mn

            option_a = NEG
            if best_one_remove is not None:
                option_a = best_zero - best_one_remove

            # merge option: removing a 1-run fuses its two zero-neighbors into one fillable block
            A, B = rid_l + 1, rid_r - 1
            best_merge = NEG
            if A <= B:
                if A == B:
                    if runs[A][0] == '1':
                        best_merge = max(best_merge, left_len + right_len)
                else:
                    if runs[A][0] == '1':
                        best_merge = max(best_merge, left_len + run_len(A + 1))
                    if runs[B][0] == '1':
                        best_merge = max(best_merge, run_len(B - 1) + right_len)
                    if A + 1 <= B - 1:
                        best_merge = max(best_merge, query_max(merge_table, A + 1, B - 1))

            best_gain = max(0, option_a, best_merge)
            if best_gain == NEG:
                best_gain = 0
            ans.append(whole_total + best_gain)

        return ans