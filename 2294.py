class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 1
        base = nums[0]
        for i in range(1, n):
            if nums[i] - base > k:
                res += 1
                base = nums[i]
        return res
