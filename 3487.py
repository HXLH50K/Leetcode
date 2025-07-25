class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = set(nums)
        if max(nums) < 0:
            return max(nums)
        return sum([x for x in nums if x > 0])
