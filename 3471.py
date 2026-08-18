from typing import List
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            for x in sorted(list(set(nums)), reverse=True):
                if nums.count(x) == 1:
                    return x
            return -1
        first = nums[0]
        last = nums[-1]
        first_cnt = nums.count(first)
        last_cnt = nums.count(last)

        if first_cnt > 1 and last_cnt > 1:
            return -1
        if first_cnt > 1:
            return last
        if last_cnt > 1:
            return first
        return max(last, first)
        