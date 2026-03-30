# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkValid(self, root, interval: list):
        if root.val >= interval[1]:
            self.res = False
            return
        if root.val <= interval[0]:
            self.res = False
            return
        
        if root.left:
            left_interval = [interval[0], root.val]
            self.checkValid(root.left, left_interval)
            if self.res == False:
                return
        if root.right:
            right_interval = [root.val, interval[1]]
            self.checkValid(root.right, right_interval)
            if self.res == False:
                return
        self.res = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        interval = [float('-inf'), float('inf')]
        self.res = True
        self.checkValid(root, interval)

        return self.res
        