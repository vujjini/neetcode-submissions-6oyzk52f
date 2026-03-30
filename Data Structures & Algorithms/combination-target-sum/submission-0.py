class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        subset = []
        res = []

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            elif i >= len(nums) or curr_sum > target:
                return
            
            subset.append(nums[i])
            dfs(i, curr_sum + nums[i])
            
            subset.pop()
            dfs(i + 1, curr_sum)

        
        dfs(0, 0)
        return res