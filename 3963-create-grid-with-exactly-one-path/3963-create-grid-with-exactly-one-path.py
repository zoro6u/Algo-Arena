from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # Top row and last column are free; everything else is an obstacle.
        # The only way to leave the top row downward is the last column, so the path is forced.
        grid = []
        for i in range(m):
            if i == 0:
                grid.append("." * n)
            else:
                grid.append("#" * (n - 1) + ".")
        return grid