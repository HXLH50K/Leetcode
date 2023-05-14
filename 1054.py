# %%
from typing import List
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) == 1:
            return barcodes
        cnter = Counter(barcodes)
        res = []
        barcodes = list(cnter.items())
        while len(barcodes) >= 2:
            barcodes.sort(key=lambda x: -x[1])
            num0, cnt0 = barcodes[0]
            num1, cnt1 = barcodes[1]
            if cnt0 == 0 or cnt2 == 0:
                break
            res.append(num0)
            res.append(num1)
            barcodes[0] = (num0, cnt0 - 1)
            barcodes[1] = (num1, cnt1 - 1)
        num0, cnt0 = barcodes[0]
        if cnt0 > 0:
            res.append(num0)

        return res


barcodes = [1, 1, 1, 2, 2, 2]
Solution().rearrangeBarcodes(barcodes)

# %%
