# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # keep track of each element from preorder list
        # first element of preorder is root
        # call a function on both sides of root
        # have the function recursvely form the subtrees and return the root 
        # finally combine the final subtress under the main root

        self.occ = {}
        for i in range(len(preorder)):
            self.occ[preorder[i]] = i

        
        def dnc(curr_arr):
            if len(curr_arr) == 0:
                return
            root_ind = 0
            for i in range(len(curr_arr)):
                if self.occ[curr_arr[i]] < self.occ[curr_arr[root_ind]]:
                    root_ind = i
            
            leftSubTree = dnc(curr_arr[:root_ind])
            rightSubTree = dnc(curr_arr[root_ind + 1:])

            return TreeNode(curr_arr[root_ind], leftSubTree, rightSubTree)
        
        return dnc(inorder)

            