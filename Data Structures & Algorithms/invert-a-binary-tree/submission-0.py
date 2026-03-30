# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # perform a recursive pre order traversal
        # for each root:
        #   swap the children
        #   do the same for its left child
        #   same for the right child
        #   if Null, go back

        def dfs(node):
            if not node:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return root