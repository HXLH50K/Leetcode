# %%
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        n = len(people)
        people.sort()
        l, r = 0, n - 1
        while l < r:
            while l < r and people[l] + people[r] > limit:
                r -= 1
                res += 1
            while l < r and people[l] + people[r] <= limit:
                r -= 1
                l += 1
                res += 1

        return res if l != r else res + 1


a = Solution()
a.numRescueBoats(people=[1, 2], limit=3)

# %%
