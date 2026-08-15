from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        if xor != 0:
            return len(nums)
        if all(num == 0 for num in nums):
            return 0
        return len(nums) - 1
