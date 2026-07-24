class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        M = 1
        while M <= max(nums):
            M <<= 1

        vals = list(set(nums))          
        n = len(vals)

        pair = bytearray(M)
        for i in range(n):
            vi = vals[i]
            for j in range(i, n):
                pair[vi ^ vals[j]] = 1

        res = bytearray(M)
        for p in range(M):
            if pair[p]:
                for v in vals:
                    res[p ^ v] = 1

        return sum(res)