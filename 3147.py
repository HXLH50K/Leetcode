# %%
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        energys = [-float("inf")] * k
        for i in range(n):
            if energys[i % k] < 0:
                energys[i % k] = energy[i]
            else:
                energys[i % k] += energy[i]
        return max(energys)


Solution().maximumEnergy([5, 2, -10, -5, 1], 3)

# %%
