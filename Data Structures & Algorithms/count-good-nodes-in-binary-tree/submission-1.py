# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countGoodNodes(self, root, max_val):
        if not root:
            return 0
        
        max_val = max(max_val, root.val)
        add = 1 if max_val == root.val else 0
        return add + self.countGoodNodes(root.left, max_val) + self.countGoodNodes(root.right, max_val)
        
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.countGoodNodes(root, root.val)