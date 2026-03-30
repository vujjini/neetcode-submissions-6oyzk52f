# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # for each node:
        #   get max_depth on right side = dfs(node.right)
        #   get max_depth on left side = dfs(node.left)
        #   add em and update res
        #   retunr the max_depth from that node

        self.res = 0

        def dfs(node):
            if not node:
                return 0
            right_depth = dfs(node.right)
            left_depth = dfs(node.left)

            self.res = max(self.res, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)

        return self.res
