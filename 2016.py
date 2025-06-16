class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        res = -1
        for i in range(n - 1):
            if right_max[i + 1] > nums[i]:
                res = max(res, right_max[i + 1] - nums[i])
        return res
