# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            
            if root.left or root.right:
                if root.left:
                    root.left = dfs(root.left)
                if root.right:
                    root.right = dfs(root.right)
            if not root.left and not root.right and root.val == target:
                root = None
            
            return root
        
        return dfs(root)