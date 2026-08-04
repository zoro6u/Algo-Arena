class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)                 # O(1) membership tests
        lo, hi = min(nums), max(nums)       # endpoints survived => this IS the range
        return [x for x in range(lo, hi + 1) if x not in present]