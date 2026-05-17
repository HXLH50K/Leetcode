from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        root = TreeNode(start)
        visited[start] = True
        queue = [root]
        while queue:
            node = queue.pop(0)
            if arr[node.val] == 0:
                return True
            for next_node in [node.val + arr[node.val], node.val - arr[node.val]]:
                if 0 <= next_node < n and not visited[next_node]:
                    visited[next_node] = True
                    queue.append(TreeNode(next_node))
        return False