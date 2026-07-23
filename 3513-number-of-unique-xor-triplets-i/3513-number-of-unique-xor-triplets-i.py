class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n < 4:
            vals = set()
            for i in range(n):
                for j in range(i, n):
                    for k in range(j, n):
                        vals.add(nums[i] ^ nums[j] ^ nums[k])
            return len(vals)
        b = n.bit_length()
        return 1 << b
    