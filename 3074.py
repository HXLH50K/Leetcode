from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum_apples = sum(apple)
        capacity.sort(reverse=True)
        cnt = 0
        for cap in capacity:
            sum_apples -= cap
            cnt += 1
            if sum_apples <= 0:
                return cnt
        return cnt
