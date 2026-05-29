from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for num in nums:
            res = min(res, sum(map(int, str(num))))
        return res