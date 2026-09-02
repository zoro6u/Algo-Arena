class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # provably always true — see derivation: with 0 odd numbers "all even"
        # trivially works; with exactly 1 odd number "all odd" works (that odd
        # number satisfies its own requirement); with >=2 odd numbers "all even" works.
        return True