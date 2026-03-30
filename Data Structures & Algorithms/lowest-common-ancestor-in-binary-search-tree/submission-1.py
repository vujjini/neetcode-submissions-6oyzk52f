# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLCA(self, root):
        if self.p.val > root.val and self.q.val > root.val:
            self.findLCA(root.right)
            return
        if self.p.val < root.val and self.q.val < root.val:
            self.findLCA(root.left)
            return
        self.res = root
        return


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p
        self.q = q
        self.res = 101
        self.findLCA(root)
        return self.res