from typing import List
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        maxl = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]+1:
                maxl += 1
            else:
                break

        summ = sum(nums[:maxl])

        nums_set = set(nums)

        while True:
            if summ in nums_set:
                summ += 1
            else:
                return summ
