# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            leftSol = dfs(node.left)
            rightSol = dfs(node.right)

            nextPath = max(leftSol, rightSol)

            currSol = max(node.val, node.val + nextPath)

            self.res = max(self.res, currSol, node.val + leftSol + rightSol)

            return currSol

        dfs(root)

        return self.res