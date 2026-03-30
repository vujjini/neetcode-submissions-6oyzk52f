# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []

        q = deque()
        q.append(root)

        while q:
            n = len(q)
            for i in range(n):
                top = q.popleft()
                if i == n - 1:
                    res.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        
        return res