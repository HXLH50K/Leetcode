from typing import List
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums.pop(0)]
        arr2 = [nums.pop(0)]
        while nums:
            x = nums.pop(0)
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)
        return arr1 + arr2