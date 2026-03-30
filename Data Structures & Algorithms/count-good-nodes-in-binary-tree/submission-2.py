# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(node, max_ancestor):
            if not node:
                return
            
            if node.val >= max_ancestor:
                self.res+=1
                max_ancestor = node.val
            
            dfs(node.left, max_ancestor)
            dfs(node.right, max_ancestor)
        
        dfs(root, -101)

        return self.res