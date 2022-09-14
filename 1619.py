# %%
from typing import List


class Solution:

    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        new_arr = arr[n // 20:19 * n // 20]
        return sum(new_arr) / len(new_arr)
