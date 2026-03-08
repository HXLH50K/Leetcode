from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(2**n):
            s = bin(i)[2:].zfill(n)
            if s not in nums:
                return s
        return ""
