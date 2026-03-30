# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        # for each node:
        #  if both p and q together are on either side of the node, go there
        #  else, the curr node is the LCA
        # edge cases:
        #  if curr_node itself is either p or q, then it is the LCA


        def dfs(node):
            if not node:
                return
            if node.val == p.val or node.val == p.val:
                return node
            
            if min(p.val, q.val) > node.val:
                return dfs(node.right)
            elif max(p.val, q.val) < node.val:
                return dfs(node.left)
            else:
                return node
        
        return dfs(root)
        
        


        
