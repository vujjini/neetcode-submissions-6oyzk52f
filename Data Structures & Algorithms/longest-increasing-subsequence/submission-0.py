class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for i in range(len(nums))]
        res = 1


        for i in range(len(nums)):
            currLen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    currLen = max(currLen, 1 + dp[j])
            dp[i] = currLen
            res = max(dp[i], res)
        
        return res
        
        
