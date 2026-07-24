from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = set()
        n = len(nums)
        double_xor = set()
        for i in range(n):
            for j in range(i, n):
                xor_value = nums[i] ^ nums[j]
                double_xor.add(xor_value)
        for k in range(n):
            for xor_value in double_xor:
                res.add(nums[k] ^ xor_value)

        return len(res)
        