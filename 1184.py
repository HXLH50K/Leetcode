# %%
from typing import List


class Solution:

    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        a = sum(distance[start:destination])
        b = sum(distance) - a
        return min(a, b)
