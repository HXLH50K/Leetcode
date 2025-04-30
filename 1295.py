class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            if x == 100000 or x < 10000 and x >= 1000 or x < 100 and x >= 10:
                res += 1
        return res
