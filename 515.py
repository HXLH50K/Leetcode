# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        queue = [[root], []]
        while True:
            ans = -inf
            for p in queue[0]:
                ans = max(p.val, ans)
            res.append(ans)
            while queue[0]:
                p = queue[0][0]
                if p.left:
                    queue[1].append(p.left)
                if p.right:
                    queue[1].append(p.right)
                queue[0].pop(0)
            if queue[1]:
                queue[0], queue[1] = queue[1], queue[0]
            else:
                break
        return res
