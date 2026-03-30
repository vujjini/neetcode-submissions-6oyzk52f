class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        subset = []
        res = []
        # [1, 2, 2, 4, 5, 6]
        nums.sort()

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            elif i >= len(nums) or curr_sum > target:
                return
            
            subset.append(nums[i])
            dfs(i + 1, curr_sum + nums[i])
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i+=1
            
            dfs(i + 1, curr_sum)

        
        dfs(0, 0)
        return res