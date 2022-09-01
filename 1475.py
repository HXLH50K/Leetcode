# %%
from typing import List


# %%
class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices


a = Solution()
a.finalPrices([9, 1, 1, 6])
