# %%
from typing import List


class Solution:
    def dfs(self, i, re):
        if i == self.n:
            self.res.append(re + [i])
            return
        for j in self.graph[i]:
            self.dfs(j, re + [i])

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph) - 1
        self.graph = graph
        self.res = []
        self.dfs(0, [])
        return self.res


a = Solution()
a.allPathsSourceTarget([[1, 3], [2], [3], []])

|# %%
