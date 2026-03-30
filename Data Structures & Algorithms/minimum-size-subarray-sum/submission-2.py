class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0

        curr_sum = nums[l]
        if curr_sum >= target:
            return 1
        res = float('inf')

        for r in range(1, len(nums)):
            curr_sum+=nums[r]
            while curr_sum >= target:
                res = min(res, r - l + 1)
                curr_sum-=nums[l]
                l+=1
            
        return res if res != float('inf') else 0
            

