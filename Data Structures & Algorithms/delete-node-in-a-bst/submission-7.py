# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return
        def findMin(root):
            if root.left:
                return findMin(root.left)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                successor = findMin(root.right)
                tmp = root.val
                root.val = successor.val
                successor.val = tmp
                root.right = self.deleteNode(root.right, key)
            elif root.left or root.right:
                if root.left:
                    root.val = root.left.val
                    root.left = None
                else:
                    root.val = root.right.val
                    root.right = None
            else:
                root = None
        return root

        