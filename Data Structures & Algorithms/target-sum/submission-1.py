class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        # rec(i, currSum) = rec(i + 1, currSum + nums[i]) + rec(i + 1, currSum - nums[i])
        # if currSum == target: return 1
        # if i >= len(nums): return 0

        cache = {}

        def dp(i, currSum):
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            if i >= len(nums):
                if currSum == target:
                    return 1
                return 0
            
            return dp(i + 1, currSum + nums[i]) + dp(i + 1, currSum - nums[i])
        
        return dp(0, 0)