class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_increase = 1
        max_decrease = 1
        current_increase = 1
        current_decrease = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_increase += 1
            else:
                current_increase = 1
            if nums[i] < nums[i-1]:
                current_decrease += 1
            else:
                current_decrease = 1
            max_increase = max(max_increase, current_increase)
            max_decrease = max(max_decrease, current_decrease)
        return max(max_increase, max_decrease)