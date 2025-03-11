class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        l_max = [float("inf")] * n
        r_min = [float("-inf")] * n
        l_max[0] = nums[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], nums[i])
        r_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            r_min[i] = min(r_min[i + 1], nums[i])
        res = 0
        for i in range(1, n - 1):
            if l_max[i - 1] < nums[i] and nums[i] < r_min[i + 1]:
                res += 2
            elif nums[i - 1] < nums[i] and nums[i] < nums[i + 1]:
                res += 1
        return res
