class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def rec(subset):
            if len(subset) == 1:
                return [subset]
            
            left = subset[0]
            perms = rec(subset[1:])
            curr_perms = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    curr_perms.append(perm[:i] + [left] + perm[i:])
            
            return curr_perms
        
        return rec(nums)
    