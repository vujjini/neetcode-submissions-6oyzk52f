# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""
        res = []

        q = deque()
        q.append(root)

        while q:
            top = q.popleft()
            if not top:
                res.append('n')
                continue
            res.append(str(top.val))
            res.append(',')
            
            q.append(top.left)
            q.append(top.right)
        print("".join(res))
        
        return "".join(res)
            
        
     # "1,2,3,nn4,5,nnnn"
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if len(data) == 0:
            return None

        nums = []

        i = 0

        while i < len(data):
            if data[i] == 'n':
                nums.append(None)
            elif data[i] == '-' or (data[i] >= '0' and data[i] <= '9'):
                curr_num = ""
                while data[i] != ',':
                    curr_num+=data[i]
                    print(curr_num)
                    i+=1
                nums.append(curr_num)
            i+=1
        print(nums)
        n = len(nums)
        
        root = TreeNode(nums[0])

        q = deque()
        q.append(root)

        i = 1
        #  [1, 2, 3, None, None, 4, 5, None, None, None, None]
        # []

        while i < n - 1:
            top = q.popleft()
            if nums[i]:
                top.left = TreeNode(int(nums[i]))
                q.append(top.left)
            i+=1
            if nums[i]:
                top.right = TreeNode(int(nums[i]))
                q.append(top.right)
            i+=1
        
        return root







