class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            hl = height[l]
            hr = height[r]
            if hl < hr:
                area = hl * (r - l)
                if area > best:
                    best = area
                l += 1
            else:
                area = hr * (r - l)
                if area > best:
                    best = area
                r -= 1
        return best