import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        loc = -1
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            if x in s:
                loc = i
                break
            s.add(x)
        if loc == -1:
            return 0
        return math.ceil((loc + 1) / 3)
