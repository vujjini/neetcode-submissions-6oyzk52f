# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue in every odd level

        if not root:
            return []
        
        res = []

        q = deque()
        q.append(root)

        while q:
            n = len(q)

            level = deque()

            for i in range(n):
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                if len(res) % 2 == 0:
                    level.append(top.val)
                else:
                    level.appendleft(top.val)
            
            res.append(level)

        return res
                
                
