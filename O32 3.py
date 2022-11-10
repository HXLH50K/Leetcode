# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [[root],[]]
        while q[0]:
            re = []
            for node in q[0]:
                re.append(node.val)
                if node.left:
                    q[1].append(node.left)
                if node.right:
                    q[1].append(node.right)
            res.append(re)
            q = [q[1],[]]
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        return res