class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(-1, len(nums) - 1):
            res = max(res, abs(nums[i] - nums[i + 1]))
        return res
