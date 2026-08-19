# %%
from typing import List
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                row_masks[row] = row_masks.get(row, 0) | 1 << (seat - 2)

        res = (n - len(row_masks)) * 2
        left = 0b00001111
        middle = 0b00111100
        right = 0b11110000

        for mask in row_masks.values():
            if mask & left == 0 and mask & right == 0:
                res += 2
            elif mask & left == 0 or mask & middle == 0 or mask & right == 0:
                res += 1

        return res

n = 4
reservedSeats = [[2,10],[3,1],[1,2],[2,2],[3,5],[4,1],[4,9],[2,7]]
solution = Solution()
print(solution.maxNumberOfFamilies(n, reservedSeats))  # Output: 4