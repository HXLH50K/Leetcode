class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = -1
        i = 0
        j = 0
        window = dict()
        while j < len(nums):
            if nums[j] not in window:
                window[nums[j]] = 0
            window[nums[j]] += 1
            while window[nums[j]] > 1:
                window[nums[i]] -= 1
                if window[nums[i]] == 0:
                    del window[nums[i]]
                i += 1
            res = max(res, sum(window.keys()))
            j += 1
        return res
