class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')

        curr_sum = 0

        for num in nums:
            curr_sum+=num
            if curr_sum < num:
                curr_sum = num
            res = max(res, curr_sum)
        
        return res