from typing import List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, index, val, childs=None):
        self.val = val
        self.index = index
        self.childs = childs if childs is not None else []

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        visited = [False] * n

        val_to_index = defaultdict(list)
        for i, val in enumerate(arr):
            val_to_index[val].append(i)

        root = TreeNode(0, arr[0])
        visited[0] = True
        queue = deque([root])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for j in [node.index + 1, node.index - 1] + val_to_index[node.val]:
                    if 0 <= j < n and not visited[j]:
                        child = TreeNode(j, arr[j])
                        node.childs.append(child)
                        if j == n - 1:
                            return steps
                        visited[j] = True
                        queue.append(child)
                val_to_index.pop(node.val, None)