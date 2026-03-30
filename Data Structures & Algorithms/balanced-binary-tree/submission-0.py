# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def get_depth(self, root):
        if not self.res:
            return 0
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth - right_depth > 1 or right_depth - left_depth > 1:
            self.res = False
            return 0
        return 1 + max(left_depth, right_depth)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.get_depth(root)
        
        return self.res