# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # for each node:
        #   there exists a bound
        #   if the val of that node is past those bounds, return False
        #   else, validate both the subtrees of that node
        #   if going left, update the upper bound, if going right update the lower bound

        def dfs(node, bounds):
            if not node:
                return True
            
            if node.val <= bounds[0] or node.val >= bounds[1]:
                return False
            
            return dfs(node.left, [bounds[0], node.val]) and dfs(node.right, [node.val, bounds[1]])

        return dfs(root, [float('-inf'), float('inf')]) 