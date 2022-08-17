# %%
from typing import List, Optional
# %%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def clean_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None or root.val is None:
        root = None
        return
    root.left = clean_tree(root.left)
    root.right = clean_tree(root.right)
    return root

def build_tree(arr: List[int]) -> Optional[TreeNode]:
    if not arr:
        return None
    root = TreeNode(arr.pop(0))
    q = [root]
    while q:
        node = q.pop(0)
        if node.val and arr:
            node.left = TreeNode(arr.pop(0))
            q.append(node.left)
        if node.val and arr:
            node.right = TreeNode(arr.pop(0))
            q.append(node.right)
    root = clean_tree(root)
    return root
# %%
if __name__ == "__main__":
    arr = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    t = build_tree(arr)
# %%
