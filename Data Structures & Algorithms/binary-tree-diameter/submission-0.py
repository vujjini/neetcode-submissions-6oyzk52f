# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_diameter(self, root):
        if not root:
            return 0
        left_diameter = self.get_diameter(root.left)
        right_diameter = self.get_diameter(root.right)
        self.diameter = max(left_diameter + right_diameter, self.diameter)

        return 1 + max(left_diameter, right_diameter)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = -1

        self.get_diameter(root)

        return self.diameter