from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        increase = True
        cnt = 0
        if n == 3:
            return False
        if nums[0] > nums[1]:
            return False
        if nums[-1] < nums[-2]:
            return False
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return False
            if increase:
                if nums[i] < nums[i + 1]:
                    continue
                else:
                    cnt += 1
                    if cnt == 3:
                        return False
                    increase = False
            else:
                if nums[i] > nums[i + 1]:
                    continue
                else:
                    cnt += 1
                    if cnt == 3:
                        return False
                    increase = True
        return cnt == 2
