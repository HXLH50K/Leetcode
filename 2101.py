# %%
from typing import List
from collections import defaultdict


class Solution:
    def in_range(self, bomb1, bomb2):
        return (bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) ** 2 <= bomb1[2] ** 2

    def bfs(self, node):
        self.visited[node] = True
        self.queue.append(node)
        while self.queue:
            node = self.queue.pop(0)
            self.re += 1
            for i in self.graph[node]:
                if not self.visited[i]:
                    self.visited[i] = True
                    self.queue.append(i)

        self.res = max(self.res, self.re)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if self.in_range(bombs[i], bombs[j]):
                    self.graph[i].append(j)

        self.res = 0
        for i in range(len(bombs)):
            self.visited = [False] * len(bombs)
            self.queue = []
            self.re = 0
            self.bfs(i)

        return self.res


bombs = [[2, 1, 3], [6, 1, 4]]
Solution().maximumDetonation(bombs)  # 2

# %%
