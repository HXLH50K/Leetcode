class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            num_sum = num % 10 + (num // 10) % 10 + (num // 100) % 10 + (num // 1000) % 10
            if num_sum == i:
                return i
        return -1