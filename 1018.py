class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        r = 0
        for num in nums:
            r = (r * 2 + num) % 5
            res.append(r == 0)
        return res
