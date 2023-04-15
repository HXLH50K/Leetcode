from typing import List
from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        graph = defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        for i in range(1, n + 1):
            colors[i] = ({1, 2, 3, 4} - {colors[j] for j in graph[i]}).pop()
        return [colors[i + 1] for i in range(n)]
