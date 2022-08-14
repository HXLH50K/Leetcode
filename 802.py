# %%
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        def dfs(i):
            if color[i] >= 1:
                return color[i] == 2
            color[i] = 1
            for j in range(len(graph[i])):
                if not dfs(graph[i][j]):
                    return False
            else:
                color[i] = 2
                return True
        for i in range(n):
            dfs(i)
        return [i for i in range(n) if color[i]==2]
a = Solution()
a.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]])
# %%
