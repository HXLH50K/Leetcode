# %%
from typing import List


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        answers = []
        for x0, y0, r in queries:
            ans = 0
            for x, y in points:
                if (x - x0) ** 2 + (y - y0) ** 2 <= r**2:
                    ans += 1
            answers.append(ans)
        return answers
