# %%
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return list(list(zip(*sorted(zip(names, heights), key=lambda x: -x[1])))[0])


Solution().sortPeople(
    ["Alex", "Ben", "Cindy", "Diana", "Eric", "Frank"], [180, 190, 170, 165, 175, 185]
)

# %%
