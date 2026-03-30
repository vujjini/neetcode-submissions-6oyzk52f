# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        # get the Inorder traversal for both
        # if subRoot exists as a subset (sliding window)

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
            return False

        start = None
        q = deque()
        q.append(root)

        while q:
            top = q.popleft()
            if top.val == subRoot.val:
                start = top
                if dfs(start, subRoot):
                    return True
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        
        return False
        