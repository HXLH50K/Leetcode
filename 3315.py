from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
                continue
            b = bin(x)[2:]
            right_most_zero = b.rfind("0")
            if right_most_zero == -1:
                b = "0" + b
                right_most_zero = 0
            n = len(b)
            right_most_zero = n - right_most_zero - 2
            an = x - (1 << right_most_zero)
            ans.append(an)
        return ans
