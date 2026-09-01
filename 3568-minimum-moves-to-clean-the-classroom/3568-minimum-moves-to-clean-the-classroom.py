from typing import List
from collections import deque
import array

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        grid = classroom

        litter_pos = []
        start = None
        for r in range(m):
            row = grid[r]
            for c in range(n):
                ch = row[c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter_pos.append((r, c))

        k = len(litter_pos)
        if k == 0:
            return 0
        litter_bit_of = {}
        for i, pos in enumerate(litter_pos):
            litter_bit_of[pos[0] * n + pos[1]] = i
        full_mask = (1 << k) - 1

        sr, sc = start
        start_cell_id = sr * n + sc
        start_mask = 1 << litter_bit_of[start_cell_id] if start_cell_id in litter_bit_of else 0
        if start_mask == full_mask:
            return 0

        num_cells = m * n
        num_masks = full_mask + 1
        best_energy = array.array('i', [-1]) * (num_cells * num_masks)

        def idx(cell_id, mask):
            return cell_id * num_masks + mask

        best_energy[idx(start_cell_id, start_mask)] = energy

        is_obstacle = bytearray(num_cells)
        is_reset = bytearray(num_cells)
        for r in range(m):
            row = grid[r]
            for c in range(n):
                cid = r * n + c
                if row[c] == 'X':
                    is_obstacle[cid] = 1
                elif row[c] == 'R':
                    is_reset[cid] = 1

        q = deque([(sr, sc, energy, start_mask, 0)])

        while q:
            r, c, e, mask, dist = q.popleft()
            if e <= 0:
                continue

            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                cid = nr * n + nc
                if is_obstacle[cid]:
                    continue
                ne = energy if is_reset[cid] else e - 1
                nmask = mask | (1 << litter_bit_of[cid]) if cid in litter_bit_of else mask
                if nmask == full_mask:
                    return dist + 1
                key = idx(cid, nmask)
                if ne > best_energy[key]:
                    best_energy[key] = ne
                    q.append((nr, nc, ne, nmask, dist + 1))

        return -1