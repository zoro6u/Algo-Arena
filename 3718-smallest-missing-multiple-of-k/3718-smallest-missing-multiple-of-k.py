class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = set(nums)
        m = k
        while m in present:
            m += k
        return m