from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        minnum = min(nums)
        maxnum = max(nums)
        missing_elements = []
        for num in range(minnum, maxnum + 1):
            if num not in nums_set:
                missing_elements.append(num)
        return missing_elements