from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(set(arr))
        rank_dict = {num: rank + 1 for rank, num in enumerate(arr_sorted)}
        return [rank_dict[num] for num in arr]