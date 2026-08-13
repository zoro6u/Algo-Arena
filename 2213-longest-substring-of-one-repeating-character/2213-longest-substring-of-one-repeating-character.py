from typing import List

class Node:
    __slots__ = ('length', 'pref', 'suf', 'best', 'lc', 'rc')
    def __init__(self, length, pref, suf, best, lc, rc):
        self.length = length
        self.pref = pref     # run of lc starting at the left edge
        self.suf = suf       # run of rc ending at the right edge
        self.best = best     # longest single-char run in this range
        self.lc = lc         # leftmost character
        self.rc = rc         # rightmost character

def merge(L: Node, R: Node) -> Node:
    length = L.length + R.length
    best = max(L.best, R.best)
    if L.rc == R.lc:                       # a run can cross the boundary
        best = max(best, L.suf + R.pref)

    pref = L.length + R.pref if (L.pref == L.length and L.rc == R.lc) else L.pref
    suf = R.length + L.suf if (R.suf == R.length and R.lc == L.rc) else R.suf

    return Node(length, pref, suf, best, L.lc, R.rc)


class SegTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.tree = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, node, lo, hi):
        if lo == hi:
            c = self.s[lo]
            self.tree[node] = Node(1, 1, 1, 1, c, c)
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid)
        self._build(2 * node + 1, mid + 1, hi)
        self.tree[node] = merge(self.tree[2 * node], self.tree[2 * node + 1])

    def _update(self, node, lo, hi, idx, ch):
        if lo == hi:
            self.tree[node] = Node(1, 1, 1, 1, ch, ch)
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            self._update(2 * node, lo, mid, idx, ch)
        else:
            self._update(2 * node + 1, mid + 1, hi, idx, ch)
        self.tree[node] = merge(self.tree[2 * node], self.tree[2 * node + 1])

    def set_char(self, idx, ch):
        if self.s[idx] == ch:
            return                          # no-op update, skip the walk
        self.s[idx] = ch
        self._update(1, 0, self.n - 1, idx, ch)

    def best(self):
        return self.tree[1].best


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegTree(s)
        result = []
        for c, idx in zip(queryCharacters, queryIndices):
            st.set_char(idx, c)
            result.append(st.best())
        return result